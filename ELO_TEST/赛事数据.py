import openpyxl

# 读取excel文件
workbook = openpyxl.load_workbook('../lpl春季赛常规赛积分.xlsx')
sheet = workbook['Sheet1']
sheet['A1'] = '队伍A'
sheet['B1'] = '队伍B'
sheet['C1'] = 'A胜场'
sheet['D1'] = 'B胜场'
file = open('../abc.txt', mode='r', encoding='utf-8')
str = []
str1 = []
str1 = file.read().split("\n")
print(str1)
file.close()
for i in range(len(str1)):
    if str1[i] != "":
        str.append(str1[i])

print(str)
i = 0
for i in range(0, len(str), 5):
    a = str[i]
    b = str[i + 2]
    c = str[i + 1].split(":")
    print(a, b, c)
    sheet.append([a, b, c[0], c[1]])

workbook.save('../lpl春季赛常规赛积分.xlsx')
