import os
import time
from buffTranslations import translate
from buffIds import description

with open("C:\\Wuthering Waves\\Wuthering Waves Game\\Client\\Saved\\Logs\\Client.log", "r", encoding="utf-8") as file:
    logs = file.read().splitlines()

debug = False
currIndex = len(logs)
currentBuffs = []

# 本地添加buff = Local buff added
# 本地移除buff = Local buff removed
#[2024.06.18-23.47.31:423][744][GameThread]Puerts: Display: (0x0000000055A87E10) [127367][I][CombatInfo][WCL][242022][23.47.31:422] [Buff][EntityId:18788:Player:BP_Anke_C_2147220767] 本地添加buff [buffId: 30000002002][创建者id: 18788][持有者: 18788][原因: 因为触发其它buff额外效果而添加（前置buff Id=30000002001, handle=1345）][handle: 268439426][前置行为id: 1196][说明: 火套-e后火伤加30%，15秒][是否迭代: true]
#[I][Loading][TL][150433][14.4.37:21] SetProgress [progress: 0]
#blendTime is the time for the camera to go back to the starting position after the ult ends, nice bait

while True:
    time.sleep(0.1)
    try:
        with open("C:\\Wuthering Waves\\Wuthering Waves Game\\Client\\Saved\\Logs\\Client.log", "r", encoding="utf-8") as file:
            logs = file.read().splitlines()
    except Exception as e:
        print("error reading file:", e.__class__)
        continue
    
    #print(len(logs)-currIndex)
    for i in range(currIndex, len(logs)):
        if(logs[i].find(" SetProgress [progress: ") != -1):                              #if you're in a loading screen
            currentBuffs = []
        if any(logs[i].find(s) == -1 for s in ["buffId: ", "Player:BP_", "[说明: "]):    #filter for buffs on the player
            continue
        if logs[i].find("服务器通过通知FightBuffComponent恢复Buff") != -1:                #these gets added when a character spawns, and never go away
            continue
            
        #desc = logs[i][logs[i].find("[说明: ")+5:]       #search for the buff description
        #desc = desc[:desc.find("]")]
        char = logs[i][logs[i].find("Player:BP_")+10:]
        char = char[:char.find("_")]
        buffId = logs[i][logs[i].find("[buffId: ")+9:]
        buffId = buffId[:buffId.find("]")]
        desc = description(buffId)

        #if any(char.isdigit() for char in desc):
        if logs[i].find("本地添加buff") != -1:        #Local buff added
            if [char,desc] not in currentBuffs and (debug or (translate(char)[:2]!="cn" and translate(desc)[:2]!="cn")):
                currentBuffs.append([char,desc])
        elif not debug and logs[i].find("本地移除buff") != -1:      #Local buff removed
            if [char,desc] in currentBuffs:
                currentBuffs.remove([char,desc])

    currIndex = len(logs)

    if not debug:
        os.system('cls')
    else:
        print("\n---------------\n")
        
    for buff in currentBuffs:
        if sum(buff[1] == b[1] for b in currentBuffs) >= 3:
            currentBuffs = list(filter(lambda b: b[1] != buff[1], currentBuffs))
            currentBuffs.append(["Team",buff[1]])

    currentBuffs = sorted(currentBuffs, key=lambda a:a[0])

    title = ""
    for buff in currentBuffs:
        if title != buff[0]:
            print("   --- "+translate(buff[0])+" ---")
            title = buff[0]
        print(translate(buff[1]))
