import ELO

print("请输入队伍A：")
A = input()
print("请输入队伍B：")
B = input()
print("BO3请输入3,BO5请输入5：")
n = input()

Ra = ELO.get_elo(A)
Rb = ELO.get_elo(B)
Ea, Eb = ELO.ELO_win_rate(Ra, Rb)

if n == '3':
    result = ELO.ELO_BO3(Ra, Rb)
    print(result)

elif n == '5':
    result = ELO.ELO_BO5(Ra, Rb)
    print(result)
