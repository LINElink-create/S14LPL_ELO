# ELO代码实现

"""ELO算法的实现"""
def ELO(Ra, Rb, Sa, K):
    # Ra: 玩家A的ELO值
    # Rb: 玩家B的ELO值
    # Sa: 玩家A的比赛结果，1表示胜利，0表示失败
    # K: K值，一般取值为32
    Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))
    Eb = 1 / (1 + 10 ** ((Ra - Rb) / 400))
    Ra = Ra + K * (Sa - Ea)
    Rb = Rb + K * ((1 - Sa) - Eb)
    return int(Ra), int(Rb)

# 计算胜率
def ELO_win_rate(Ra, Rb):
    Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))
    Eb = 1 / (1 + 10 ** ((Ra - Rb) / 400))
    return Ea, Eb

# bo3比赛
def bo3_ELO(Ra, Rb, A, B, K):
    if A == 2:
        Ra,Rb = ELO(Ra, Rb, 1, K)
        Ra,Rb = ELO(Ra, Rb, 1, K)
        if B == 1:
            Ra,Rb = ELO(Ra, Rb, 0, K)
    elif B == 2:
        Ra,Rb = ELO(Ra, Rb, 0, K)
        Ra,Rb = ELO(Ra, Rb, 0, K)
        if A == 1:
            Ra,Rb = ELO(Ra, Rb, 1, K)
    return Ra, Rb