import ELO

print("最新赛果：")
print("请输入队伍A：")
A = input()
print("请输入队伍B：")
B = input()
print("请输入队伍A胜场数：")
a = input()
print("请输入队伍B胜场数：")
b = input()

Ra = ELO.get_elo(A)
Rb = ELO.get_elo(B)
print("队伍A ELO值：", Ra)
print("队伍B ELO值：", Rb)
if int(a) == 3 or int(b) == 3:
    K = 16
    Ra, Rb = ELO.bo_n_ELO(Ra, Rb, int(a), int(b), 16)
else:
    Ra, Rb = ELO.bo_n_ELO(Ra, Rb, int(a), int(b), 32)

print("队伍A ELO值：", Ra)
print("队伍B ELO值：", Rb)



team, elo = ELO.read_elo()
elo[team.get(A)] = Ra
elo[team.get(B)] = Rb
print("若要保存输入1，否则输入任意字符：")
c = input()
if c == '1':
    ELO.save_game(A, B, a, b)
    ELO.save_elo(elo)
    print("保存成功")
else:
    print("退出")
