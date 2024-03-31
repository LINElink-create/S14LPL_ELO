# ELO代码实现

"""ELO算法的实现"""
import openpyxl


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

# bo5比赛
def bo5_ELO(Ra, Rb, A, B, K):
    if A == 3:
        Ra,Rb = ELO(Ra, Rb, 1, K)
        Ra,Rb = ELO(Ra, Rb, 1, K)
        Ra,Rb = ELO(Ra, Rb, 1, K)
        if B == 2:
            Ra,Rb = ELO(Ra, Rb, 0, K)
            Ra,Rb = ELO(Ra, Rb, 0, K)
        elif B == 1:
            Ra,Rb = ELO(Ra, Rb, 0, K)
    elif B == 3:
        Ra,Rb = ELO(Ra, Rb, 0, K)
        Ra,Rb = ELO(Ra, Rb, 0, K)
        Ra,Rb = ELO(Ra, Rb, 0, K)
        if A == 2:
            Ra,Rb = ELO(Ra, Rb, 1, K)
            Ra,Rb = ELO(Ra, Rb, 1, K)
        elif A == 1:
            Ra,Rb = ELO(Ra, Rb, 1, K)
    return Ra, Rb

def read_elo():
    workbook = openpyxl.load_workbook('../lpl春季赛常规赛积分.xlsx')
    workbook1 = openpyxl.load_workbook('../ELO积分.xlsx')
    sheet = workbook['Sheet1']
    sheet['A1'] = '队伍A'
    sheet['B1'] = '队伍B'
    sheet['C1'] = 'A胜场'
    sheet['D1'] = 'B胜场'

    sheet1 = workbook1['Sheet1']
    sheet1['A1'] = '队伍'
    sheet1['B1'] = 'ELO积分'

    team = {}
    elo = {}
    team_num = 1
    for row in sheet1.values:
        if row[0] == '队伍':
            continue
        team[row[0]] = team_num
        elo[team_num] = row[1]
        team_num += 1

    workbook.save('../lpl春季赛常规赛积分.xlsx')
    workbook1.save('../ELO积分.xlsx')
    return team, elo

def get_elo(t):
    team, elo = read_elo()
    team_num = team[t]
    return elo.get(team_num)


def save_elo(elo):
    workbook1 = openpyxl.load_workbook('../ELO积分.xlsx')
    sheet1 = workbook1['Sheet1']
    sheet1['A1'] = '队伍'
    sheet1['B1'] = 'ELO积分'
    i = 2
    for key in elo.keys():
        sheet1["B" + str(i)] = elo.get(key)
        i += 1
    workbook1.save('../ELO积分.xlsx')


def save_game(A, B, a, b):
    workbook = openpyxl.load_workbook('../lpl春季赛常规赛积分.xlsx')
    sheet = workbook['Sheet1']
    sheet.append([A, B, a, b])
    workbook.save('../lpl春季赛常规赛积分.xlsx')