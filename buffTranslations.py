def translate(s):
    dict = {
        #generic
        "Team" : "Team",
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
        "Baer" : "Mortefi",
        "监听并调用2颗龙鳞子弹buff - 全队重击用" : "14s - mortefi's coordinated attack",
        "" : "",

        #sanhua
        "Sanhua" : "Sanhua",
        "上场角色普通攻击伤害加深38%，持续14秒。角色退场删除" : "38% amplify basic - 14s - sanhua's outro,",
        "散华被动1-E技能伤害提升20%，持续8秒" : "20% skill dmg - 8s - trace 1",
        "" : "",


        "Nvzhu" : "Spectro rover",
        "" : "",
        "" : "",
        "" : "",


        "BaiLian" : "Baizhi",
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
