import os
import time
from buffTranslations import translate, ultDelay, buffTime
from buffIds import description
from datetime import datetime

gamePath = "C:\\Wuthering Waves"
logsPath = "\\Wuthering Waves Game\\Client\\Saved\\Logs\\Client.log"
logsFile = open(gamePath+logsPath, "r", encoding="utf-8")
logsFile.seek(0, os.SEEK_END)
currentBuffs = []  #[[char, desc, timer], ...]
charInPlay = ""
oldSize = os.path.getsize(gamePath+logsPath)
debug = False

# 本地添加buff = Local buff added
# 本地移除buff = Local buff removed
#[2024.06.18-23.47.31:423][744][GameThread]Puerts: Display: (0x0000000055A87E10) [127367][I][CombatInfo][WCL][242022][23.47.31:422] [Buff][EntityId:18788:Player:BP_Anke_C_2147220767] 本地添加buff [buffId: 30000002002][创建者id: 18788][持有者: 18788][原因: 因为触发其它buff额外效果而添加（前置buff Id=30000002001, handle=1345）][handle: 268439426][前置行为id: 1196][说明: 火套-e后火伤加30%，15秒][是否迭代: true]
#[I][Loading][TL][150433][14.4.37:21] SetProgress [progress: 0]

def getCurrentChar(log):
    if charInPlay == "":
        if log.find("BP_") != -1:
            s = log[log.find("BP_")+3:]
            #print(s[:s.find("_")])
            s = translate(s[:s.find("_")])
            if s[:2] != "cn":
                return s
    elif log.find("EnableCollision [CreatureDataId: ") != -1:
        if log.find("][PbDataId: ")+16<len(log) and log[log.find("][PbDataId: ")+16] == "]":
            s = log[log.find("][PbDataId: ")+12:]
            s = translate(s[:s.find("]")])
            if s[:2] != "cn":
                return s
    return charInPlay

def indexOfBuff(char,desc):
    for i, buff in enumerate(currentBuffs):
        if desc == buff[1] and (char == buff[0] or "Team" == buff[0]):
            return i
    return False

while True:
    time.sleep(0.01)

    if os.path.getsize(gamePath+logsPath) < oldSize:                            #the game make a new file after ~20MiB
        try:                                                                    #TODO: read the leftover lines of the old file
            if not logsFile.closed:
                logsFile.close()
            logsFile = open(gamePath+logsPath, "r", encoding="utf-8")
        except Exception as e:
            print("error reading file:", e.__class__)
            continue
    try:
        logs = logsFile.read().splitlines()
    except Exception as e:
        print("error reading filestream:", e.__class__)
        continue

    oldSize = os.path.getsize(gamePath+logsPath)

    for log in logs:
        charInPlay = getCurrentChar(log)
        if log.find("添加等待设置时停的tag") != -1:                                   #ult
            for buff in currentBuffs:
                buff[2] += ultDelay(charInPlay)
        if log.find(" SetProgress [progress: ") != -1:                              #if you're in a loading screen
            currentBuffs = []
        if any(log.find(s) == -1 for s in ["buffId: ", "Player:BP_", "[说明: "]):   #filter for buffs on the player
            continue
        if log.find("服务器通过通知FightBuffComponent恢复Buff") != -1:               #these gets added when a character spawns, and never go away
            continue
            
        char = log[log.find("Player:BP_")+10:]
        char = translate(char[:char.find("_")])
        buffId = log[log.find("[buffId: ")+9:]
        buffId = buffId[:buffId.find("]")]
        desc = translate(description(buffId))

        if log.find("本地添加buff") != -1:                      #Local buff added
            if not indexOfBuff(char,desc):
                if debug or (char[:2]!="cn" and desc[:2]!="cn"):
                    currentBuffs.append([char,desc,buffTime(desc)])                                                 #TODO: parse exact time the buff was added
            else:
                currentBuffs[indexOfBuff(char,desc)][2] = buffTime(desc)
        elif not debug and log.find("本地移除buff") != -1:      #Local buff removed
            if not indexOfBuff(char,desc) is False:  #to distinguish with 0
                currentBuffs.pop(indexOfBuff(char,desc))

    
    for buff in currentBuffs:
        if buff[2] != None:
            buff[2] -= (datetime.now()-oldTime).seconds + (datetime.now()-oldTime).microseconds/1000000
        if sum(buff[1] == b[1] for b in currentBuffs) >= 3:
            currentBuffs = list(filter(lambda b: b[1] != buff[1], currentBuffs))
            currentBuffs.append(["Team",buff[1],buff[2]])                                                 #TODO: exact time
    oldTime = datetime.now()

    currentBuffs = sorted(currentBuffs, key=lambda a:a[0])
    
    title = ""
    outString = ""
    for buff in currentBuffs:
        if title != buff[0]:
            title = buff[0]
            outString += "\n   --- " + title + " ---"
        outString += "\n" + buff[1]
        if buff[2] != None:
             outString += "  :  " + str(round(buff[2], 2))

    if not debug:
        os.system('cls')
    else:
        print("\n---------------\n")
        
    print(outString)
