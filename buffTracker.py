import os
import time
from functools import cmp_to_key

file = open("C:\\Wuthering Waves\\Wuthering Waves Game\\Client\\Saved\\Logs\\Client.log", "r", encoding="utf-8")
logs = file.read().splitlines()
file.close()

mode = 'white'+'list' #blacklist mainly used for testing
currIndex = len(logs)
currentBuffs = []

# 本地添加buff = Local buff added
# 本地移除buff = Local buff removed

#[2024.06.18-23.47.31:423][744][GameThread]Puerts: Display: (0x0000000055A87E10) [127367][I][CombatInfo][WCL][242022][23.47.31:422] [Buff][EntityId:18788:Player:BP_Anke_C_2147220767] 本地添加buff [buffId: 30000002002][创建者id: 18788][持有者: 18788][原因: 因为触发其它buff额外效果而添加（前置buff Id=30000002001, handle=1345）][handle: 268439426][前置行为id: 1196][说明: 火套-e后火伤加30%，15秒][是否迭代: true]
#[2024.06.18-23.48.11:733][900][GameThread]Puerts: Display: (0x0000000055A87E10) [129280][I][CombatInfo][WCL][243179][23.48.11:733] [Buff][EntityId:18822:Player:BP_Anke_C_2147204540] 本地添加buff [buffId: 30000002001][创建者id: 18822][持有者: 18822][原因: 服务器通过通知FightBuffComponent恢复Buff][handle: 13][前置行为id: undefined][说明: 火套-e后火伤加30%，15秒][是否迭代: true]

def translate(s):
    dict = {
        #generic
        "拐套-使用退场技后，下一个人攻击力+22.5%，15秒。" : "22.5% atk - 15s - moonlight set",
        "奶套-触发治疗为全队加攻15%，30秒。" : "15% atk - 30s - healing set",
        "光套-qte登场后光伤+30%，15秒" : "30% dmg - 15s - spectro set",
        "火套-e后火伤加30%，15秒" : "30% dmg - 15s - fusion set",
        "孤鸯-大招+12%，15秒" : "aix buff",
        "三头鸟-增伤12%，15秒" : "12% dmg - heron echo",
        "乌龟-增伤" : "10% dmg - 15s - bell echo",
        #"对自己的所有伤害减少50%" : "50% dmg reduction - echo",
        "" : "",
        "" : "",

        #encore
        "Anke" : "Encore",
        "安可被动1-使用E，火属性伤害提升，效果持续8秒。" : "IDK WHAT THIS IS ALOOOOOOOOOOOOOOOOO, Encore Passive 1- Using E, fire damage is increased and the effect lasts for 8 seconds.",
        "火属性伤害提升10%" : "10% dmg - 10s - encore trace",
        "攻击力提高12%，最多2层，前后台都生效" : "24% atk - 5s - Stringmaster's stacks",
        "增加自身4%热熔伤害，可叠加4层，持续6秒。" : "12% dmg - 6s - s1 encore",
        "骑士-火伤+12%，15秒" : "12% fire+basic dmg - 15s - Inferno rider",
        #"以上场角色为中心，原地留下灼烧大地，对上面的敌人每1秒造成安可攻击力270%的火元素伤害，持续6秒。" : "encore's outro",
        "" : "",
        "" : "",

        #mortefi
        "监听并调用2颗龙鳞子弹buff - 全队重击用" : "14s - mortefi's coordinated attack",
        "" : "",
        "" : "",
        "" : "",

        #sanhua
        "Sanhua" : "Sanhua",
        "上场角色普通攻击伤害加深38%，持续14秒。角色退场删除" : "38% amplify basic - 14s - sanhua's outro,",
        "散华被动1-E技能伤害提升20%，持续8秒" : "20% skill dmg - 8s - trace 1",
        "" : "",
        "" : "",
        "" : "",
        
        #verina
        "Jueyuan" : "Verina",
        "全队加攻击力20%" : "20% atk - 20s - verina trace",
        "上场角色6秒内回复绝园总共60%最大生命值的生命，效果为逐渐衰减。全队伤害加深15%，持续30秒。" : "15% dmg deep - 30s - verina's outro",
        "" : "",
        "" : ""
    }

    if s in dict:
        return dict[s]
    if mode == "whitelist":
        return ""
    return s


while True:

    time.sleep(0.1)
    try:
        file = open("C:\\Wuthering Waves\\Wuthering Waves Game\\Client\\Saved\\Logs\\Client.log", "r", encoding="utf-8")
        logs = file.read().splitlines()
        file.close()
    except:
        continue

    for i in range(currIndex, len(logs)):
        if any(logs[i].find(s) == -1 for s in ["buffId: ", "Player:BP_", "[说明: "]):   #filter for buffs on the player
            continue
        if logs[i].find("服务器通过通知FightBuffComponent恢复Buff") != -1:   #these gets added as a character spawns, and never go away
            continue

        desc = logs[i][logs[i].find("[说明: ")+5:]       #search for the buff description
        desc = desc[:desc.find("]")]
        char = logs[i][logs[i].find("Player:BP_")+10:]
        char = char[:char.find("_")]

        #if any(char.isdigit() for char in desc):
        if logs[i].find("本地添加buff") != -1:        #Local buff added
            if desc not in currentBuffs:
                currentBuffs.append([char,desc])
        elif logs[i].find("本地移除buff") != -1:      #Local buff removed
            if [char,desc] in currentBuffs:
                currentBuffs.remove([char,desc])

    currIndex = len(logs)

    os.system('cls')
    #print('-------------')
    currentBuffs = sorted(currentBuffs, key=lambda a:a[0])
    title = ""
    n = 0
    for buff in currentBuffs:
        if translate(buff[0]) == "" or translate(buff[1]) == "":
            continue
        if title != buff[0]:
            print("   --- "+translate(buff[0])+" --- ")
            title = buff[0]
            n = 0
        n += 1
        #print(str(n)+". "+translate(buff[1]))
        print(translate(buff[1]))
