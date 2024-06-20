def translate(s):
    dict = {
        #generic
        "Team" : "Team",
        #"对自己的所有伤害减少50%" : "50% dmg reduction - echo",
        #"无妄者-暗主大招后5秒内使用加伤50%" : "dreamless buffed",
        "拐套-使用退场技后，下一个人攻击力+22.5%，15秒。" : "22.5% atk - 15s - moonlight set",
        "奶套-触发治疗为全队加攻15%，30秒。" : "15% atk - 30s - healing set",
        "光套-qte登场后光伤+30%，15秒" : "30% dmg - 15s - spectro set",
        "火套-e后火伤加30%，15秒" : "30% dmg - 15s - fusion set",
        "骑士-火伤+12%，15秒" : "12% fire+basic dmg - 15s - Inferno rider",
        "孤鸯-大招+12%，15秒" : "aix buff",
        "三头鸟-增伤12%，15秒" : "12% dmg - heron echo",
        "乌龟-增伤" : "10% dmg - 15s - bell echo",
        " 无冠者分身-共鸣技能伤害+12%，15秒" : "12% havoc+skill dmg - 15s - crownless",
        "攻击力提升eog" : "6% dmg per stack - 10s - Emerald of genesis",
        "" : "",

        #encore
        "Anke" : "Encore",
        #"以上场角色为中心，原地留下灼烧大地，对上面的敌人每1秒造成安可攻击力270%的火元素伤害，持续6秒。" : "encore's outro",
        "火属性伤害提升10%" : "10% dmg - 10s - trace 1",
        "攻击力提高12%，最多2层，前后台都生效" : "24% atk - 5s - Stringmaster's stacks",
        "增加自身4%热熔伤害，可叠加4层，持续6秒。" : "12% dmg - 6s - s1 encore",
        "" : "",
        "" : "",

        #mortefi
        "Baer" : "Mortefi",
        "上场角色重击伤害加深38%，持续14秒。角色退场删除" : "14s - mortefi's coordinated attack",
        "【加强音】造成的暴击伤害提升30%。" : "Critical damage dealt by [Fortissimo] is increased by 30%.",

        #sanhua
        "Sanhua" : "Sanhua",
        "上场角色普通攻击伤害加深38%，持续14秒。角色退场删除" : "38% amplify basic - 14s - sanhua's outro",
        "散华被动1-E技能伤害提升20%，持续8秒" : "20% skill dmg - 8s - trace 1",
        "" : "",

        #Spectro rover
        "Nvzhu" : "Spectro rover",
        "变身后，解离伤害增加20%" : "surge state",
        "" : "",

        #Baizhi
        "BaiLian" : "Baizhi",
        "白芷提供医疗支援，令场上的角色每3秒回复白芷5%最大生命值的生命，持续30秒。受到此治疗效果时，还能获得全伤害加深15%的效果，持续6秒。" : "15% dmg deep - ~30s - baizhi's outro",
        "白莲被动1_加攻击力" : "20% atk - 20s - baizhi's trace",
        "白莲大招周期生成子弹" : "Coordinated attacks - baizhi",

        #verina
        "Jueyuan" : "Verina",
        "全队加攻击力20%" : "20% atk - 20s - verina's trace",
        "上场角色6秒内回复绝园总共60%最大生命值的生命，效果为逐渐衰减。全队伤害加深15%，持续30秒。" : "15% dmg deep - 30s - verina's outro",
        "" : "",
        "" : "",

        #Jiyan
        "Jiyan" : "Jiyan",
        "" : "",
        "" : "",

        #Havoc rover
        "DarkNvzhu" : "Havoc rover",
        "" : "",

        #Danjin
        "Micai" : "Danjin",
        "上场角色暗元素伤害加深23%，持续14秒。" : "Danjin's outro",
        "攻击力buff" : "30% atk at max stacks - 7s - s1",
        #cn - 暗套-普攻或者重击加暗伤7.5%，最多4层，15秒 
        #cn - 重击增伤24% - removed mechanics maybe? nothing like this is in her kit

        #Taoqi
        "Taohua" : "Taoqi",
        "上场角色技能伤害加深38%，持续14秒。角色退场删除" : "38% amplify skill - 14s - Taoqi's outro",
        "" : ""
    }

    if s in dict:
        return dict[s]
    return "cn - " + s

#the logs dont have enough about this, have to time them manually..
def ultDelays():
    dict = {
        "Sanhua" : 1.7,
        "Encore" : 2.2,
        "Verina" : 1.7
    }
    if s in dict:
        return dict[s]
    return 0
