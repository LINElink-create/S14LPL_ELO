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



def bo_n_ELO(Ra, Rb, A, B, K):
    if A>0:
        for i in range(A):
            Ra, Rb = ELO(Ra, Rb, 1, K)
    if B>0:
        for i in range(B):
            Ra, Rb = ELO(Ra, Rb, 0, K)
    return Ra, Rb

# 读取excel文件
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


def get_elo(t):
    team_num = team[t]
    return elo.get(team_num)


# 输出所有数据
for row in sheet.values:
    if row[0] == '队伍A':
        continue
    Ra = get_elo(row[0])
    Rb = get_elo(row[1])
    A = int(row[2])
    B = int(row[3])
    # K值 常规赛取32, 季后赛取16, 决赛取8, 世界赛取16, 世界赛决赛取8
    K = 32
    Ra, Rb = bo_n_ELO(Ra, Rb, A, B, K)
    print(Ra, Rb)
    elo[team.get(row[0])] = Ra
    elo[team.get(row[1])] = Rb

i = 2
for key in elo.keys():
    sheet1["B" + str(i)] = elo.get(key)
    i += 1

workbook1.save('../ELO积分.xlsx')
