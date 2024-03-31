import ELO_TEST.ELO as ELO
from scipy.stats import binom
import openpyxl

game1_winner = ""
game2_winner = ""
game3_winner = ""
game4_winner = ""
game5_winner = ""
game6_winner = ""
game7_winner = ""
game8_winner = ""
game9_winner = ""
game10_winner = ""
game11_winner = ""
game7_loser = ""
game8_loser = ""
game10_loser = ""

# 读取excel文件 获取队伍和ELO积分
workbook = openpyxl.load_workbook('../ELO积分.xlsx')
sheet = workbook['Sheet1']
sheet['A1'] = '队伍'
sheet['B1'] = 'ELO积分'

team = {}
elo = {}
team_num = 1
for row in sheet.values:
    if row[0] == '队伍':
        continue
    team[row[0]] = team_num
    elo[team_num] = row[1]
    team_num += 1


def get_elo(t):
    team_num = team[t]
    return elo.get(team_num)


def ELO_BO5(Ra, Rb):
    Ea, Eb = ELO.ELO_win_rate(Ra, Rb)
    win_rate = str(round(Ea * 100, 1))
    print("守擂者胜率为：" + win_rate + "%")
    r_3_0 = binom.pmf(3, 3, Ea)
    r_3_1 = binom.pmf(2, 3, Ea) * Ea
    r_3_2 = binom.pmf(2, 4, Ea) * Ea
    r_2_3 = binom.pmf(2, 4, Ea) * (1 - Ea)
    r_1_3 = binom.pmf(1, 3, Ea) * (1 - Ea)
    r_0_3 = binom.pmf(0, 3, Ea)

    print(f'3:0概率为: {round(r_3_0 * 100, 1)}%')
    print(f'3:1概率为: {round(r_3_1 * 100, 1)}%')
    print(f'3:2概率为: {round(r_3_2 * 100, 1)}%')
    print(f'2:3概率为: {round(r_2_3 * 100, 1)}%')
    print(f'1:3概率为: {round(r_1_3 * 100, 1)}%')
    print(f'0:3概率为: {round(r_0_3 * 100, 1)}%')

    result = {
        r_3_0: '3:0',
        r_3_1: '3:1',
        r_3_2: '3:2',
        r_2_3: '2:3',
        r_1_3: '1:3',
        r_0_3: '0:3'
    }
    return result.get(max(r_3_0, r_3_1, r_3_2, r_2_3, r_1_3, r_0_3))


def game(game_player):
    game1 = ELO_BO5(get_elo(game_player[7]), get_elo(game_player[8]))
    if game1.index('3') == 0:
        game1_winner = game_player[7]
    else:
        game1_winner = game_player[8]
    print("%s %s %s 获胜者为：%s" % (game_player[7], game1, game_player[8], game1_winner))

    game2 = ELO_BO5(get_elo(game_player[6]), get_elo(game_player[9]))
    if game2.index('3') == 0:
        game2_winner = game_player[6]
    else:
        game2_winner = game_player[9]
    print("%s %s %s 获胜者为：%s" % (game_player[6], game2, game_player[9], game2_winner))

    game3 = ELO_BO5(get_elo(game_player[4]), get_elo(game1_winner))
    if game3.index('3') == 0:
        game3_winner = game_player[4]
    else:
        game3_winner = game1_winner
    print("%s %s %s 获胜者为：%s" % (game_player[4], game3, game1_winner, game3_winner))

    game4 = ELO_BO5(get_elo(game_player[5]), get_elo(game2_winner))
    if game4.index('3') == 0:
        game4_winner = game_player[5]
    else:
        game4_winner = game2_winner
    print("%s %s %s 获胜者为：%s" % (game_player[5], game4, game2_winner, game4_winner))

    game5 = ELO_BO5(get_elo(game_player[3]), get_elo(game3_winner))
    if game5.index('3') == 0:
        game5_winner = game_player[3]
    else:
        game5_winner = game3_winner
    print("%s %s %s 获胜者为：%s" % (game_player[3], game5, game3_winner, game5_winner))

    game6 = ELO_BO5(get_elo(game_player[2]), get_elo(game4_winner))
    if game6.index('3') == 0:
        game6_winner = game_player[2]
    else:
        game6_winner = game4_winner
    print("%s %s %s 获胜者为：%s" % (game_player[2], game6, game4_winner, game6_winner))

    game7 = ELO_BO5(get_elo(game_player[0]), get_elo(game5_winner))

    if game7.index('3') == 0:
        game7_winner = game_player[0]
        game7_loser = game5_winner
    else:
        game7_winner = game5_winner
        game7_loser = game_player[0]
    print("%s %s %s 获胜者为：%s" % (game_player[0], game7, game5_winner, game7_winner))

    game8 = ELO_BO5(get_elo(game_player[1]), get_elo(game6_winner))
    if game8.index('3') == 0:
        game8_winner = game_player[1]
        game8_loser = game6_winner
    else:
        game8_winner = game6_winner
        game8_loser = game_player[1]
    print("%s %s %s 获胜者为：%s" % (game_player[1], game8, game6_winner, game8_winner))

    game9 = ELO_BO5(get_elo(game7_loser), get_elo(game8_loser))
    if game9.index('3') == 0:
        game9_winner = game7_loser
    else:
        game9_winner = game8_loser
    print("%s %s %s 获胜者为：%s" % (game7_loser, game9, game8_loser, game9_winner))

    game10 = ELO_BO5(get_elo(game7_winner), get_elo(game8_winner))
    if game10.index('3') == 0:
        game10_winner = game7_winner
        game10_loser = game8_winner
    else:
        game10_winner = game8_winner
        game10_loser = game7_winner
    print("%s %s %s 获胜者为：%s" % (game7_winner, game10, game8_winner, game10_winner))

    game11 = ELO_BO5(get_elo(game9_winner), get_elo(game10_loser))
    if game11.index('3') == 0:
        game11_winner = game9_winner
    else:
        game11_winner = game10_loser
    print("%s %s %s 获胜者为：%s" % (game9_winner, game11, game10_loser, game11_winner))

    print("冠军为：%s" % game10_winner, "亚军为：%s" % game11_winner)
