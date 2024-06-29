def translate(s):
    dict = {
        #generic
        "Team" : "Team",
        #"对自己的所有伤害减少50%" : "50% dmg reduction - echo",
        #"无妄者-暗主大招后5秒内使用加伤50%" : "dreamless buffed",
        "拐套-使用退场技后，下一个人攻击力+22.5%，15秒。" : "22.5% atk - 15s - moonlight set",
        "奶套-触发治疗为全队加攻15%，30秒。" : "15% atk - 30s - healing set",                   #TODO: all sets cd seems to not be refreshing
        "光套-qte登场后光伤+30%，15秒" : "30% dmg - 15s - spectro set",
        "火套-e后火伤加30%，15秒" : "30% dmg - 15s - fusion set",
        "雷套-e、重击分别使自身雷伤加15%，15秒" : "30% dmg - 15s - electro set",
        "骑士-火伤+12%，15秒" : "12% fire+basic dmg - 15s - Inferno rider echo",
        " 无冠者分身-共鸣技能伤害+12%，15秒" : "12% havoc+skill dmg - 15s - crownless echo",
        "三头鸟-增伤12%，15秒" : "12% dmg - heron echo",
        "孤鸯-大招+12%，15秒" : "aix buff",
        "乌龟-增伤" : "10% dmg - 15s - bell echo",

        #weapons    #TODO use "ModifierMagnitude" in buffs.py to check for the number of compies
        "攻击力提升eog" : "6% dmg per stack - 10s - Emerald of genesis",
        "攻击" : "4% atk per stack up to 5 - 7s - Atumtrace",
        "攻击力提高12%，最多2层，后台时生效" : "12% per stack - stringmaster background buff",

        #encore
        "Anke" : "Encore",
        #"以上场角色为中心，原地留下灼烧大地，对上面的敌人每1秒造成安可攻击力270%的火元素伤害，持续6秒。" : "encore's outro",
        "火属性伤害提升10%" : "10% dmg - 10s - trace 1",
        "攻击力提高12%，最多2层，前后台都生效" : "24% atk - 5s - Stringmaster's stacks",
        "增加自身4%热熔伤害，可叠加4层，持续6秒。" : "12% dmg - 6s - s1 encore", #so much stuff isnt refreshing
        "" : "",
        "" : "",

        #mortefi
        "Baer" : "Mortefi",#Coordinated attacks - 14s - mortefi's coordinated attack
        "上场角色重击伤害加深38%，持续14秒。角色退场删除" : "38% amplify heavy - 14s - Mortefi's outro",
        #"【加强音】造成的暴击伤害提升30%。" : "Critical damage dealt by [Fortissimo] is increased by 30%.",

        #sanhua
        "Sanhua" : "Sanhua",
        "上场角色普通攻击伤害加深38%，持续14秒。角色退场删除" : "38% amplify basic - 14s - sanhua's outro",
        "散华被动1-E技能伤害提升20%，持续8秒" : "20% skill dmg - 8s - trace 1",
        "" : "",

        #Spectro rover
        "Nvzhu" : "Spectro Rover",
        "" : "",

        #Baizhi
        "BaiLian" : "Baizhi",
        "白芷提供医疗支援，令场上的角色每3秒回复白芷5%最大生命值的生命，持续30秒。受到此治疗效果时，还能获得全伤害加深15%的效果，持续6秒。" : "15% dmg deep - 6s - baizhi's outro",
        "白莲被动1_加攻击力" : "20% atk - 20s - baizhi's trace",
        "白莲大招周期生成子弹" : "Coordinated attacks - 10s - baizhi",

        #verina
        "Jueyuan" : "Verina",
        "全队加攻击力20%" : "20% atk - 20s - Verina's trace",
        "上场角色6秒内回复绝园总共60%最大生命值的生命，效果为逐渐衰减。全队伤害加深15%，持续30秒。" : "15% dmg deep - 30s - Verina's outro",
        "" : "",
        
        #Yinlin
        "Yinlin" : "Yinlin",
        "上场角色雷元素伤害加深20%，共鸣解放伤害加深25%，持续14秒。角色退场删除" : "20% electro 25% ult aplify - 14s - Yinlin's outro",
        "暴击率提升15%，持续5s" : "15% cr - 5s - Yinlin crit rate buff",
        "吟霖核心被动机制" : "Coordinated attacks - 18s - Yinlin",
        "" : "",#TODO 2nd trace

        #Jiyan
        "Jiyan" : "Jiyan",
        "" : "",

        #Calcharo
        "Kakaluo" : "Calcharo",
        "释放非大招状态重击时，卡卡罗获得共鸣解放伤害10%，持续15秒" : "10% lib dmg - 15s - Trace 1", #TODO
        #"以上场角色为中心，释放闪电脉冲，对周围敌人造成卡卡罗攻击力781%的雷属性伤害。" : "Calcharo's outro",
        "" : "",

        #Havoc rover
        "DarkNvzhu" : "Havoc Rover", #name might be different on male char?
        "变身后，解离伤害增加20%" : "surge state",
        "" : "",

        #Danjin
        "Micai" : "Danjin",
        "上场角色暗元素伤害加深23%，持续14秒。" : "Danjin's outro",
        #"烧血BUFF1" : "30% atk at max stacks - 7s - s1",
        "暗套-普攻或者重击加暗伤7.5%，最多4层，15秒":"test 1",  #TODO
        "重击增伤24%":"test 2", #- removed mechanics maybe? nothing like this is in her kit
        "" : "",

        #Taoqi
        "Taohua" : "Taoqi",
        "上场角色技能伤害加深38%，持续14秒。角色退场删除" : "38% amplify skill - 14s - Taoqi's outro",
        "" : "",
        
        #Jinhsi
        "Jinxi" : "Jinhsi",
        "" : "",

        #ids
        "1102" : "Sanhua",
        "1103" : "Baizhi",
        "1104" : "Lingyang",
        "1202" : "Chixia",
        "1203" : "Encore",
        "1204" : "Mortefi",
        "1301" : "Calcharo",
        "1302" : "Yinlin",
        "1303" : "Yuanwu",
        "1304" : "Jinhsi",
        "1402" : "Yangyang",
        "1403" : "Aalto",
        "1404" : "Jiyan",
        "1405" : "Jianxin",
        "1501" : "Spectro Rover",
        "1502" : "Spectro Rover",
        "1503" : "Verina",
        "1601" : "Taoqi",
        "1602" : "Danjin",
        "1603" : "Camellya", #?
        "1604" : "Havoc Rover",
        "1605" : "Havoc Rover",
        "" : "",
        "" : "",
        "" : "",


    }

    if s in dict:
        return dict[s]
    return "cn - " + s

#the logs dont have enough about this, have to time them manually..
def ultDelay(s):
    dict = {
        "Sanhua" : 1.7,
        "Encore" : 2.2,
        "Verina" : 1.7,
        "Yinlin" : 3.2,
        "Calcharo" : 2,
    }
    if s in dict:
        return dict[s]
    return 0

def buffTime(s):
    s = s[s.find("-")+2:s.find("-")+s[s.find("-"):].find("s")]
    if s.isnumeric():
        return float(s)
    return None
