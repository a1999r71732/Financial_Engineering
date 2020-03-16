import math

print("本金（萬元）：")     #輸入本金
money = int(input()) * 10000

print("期數（年）：")     #輸入期數
years = int(input()) * 12

print("年利率（%）：")     #輸入年利率
rate = float(input()) * 0.01

list=[]
c = 0
c = money/years

s = 0

for i in range(years-1):         #除了最後一期之外的本金平均攤還、利息、本利和
    list.append([i+1,math.ceil(c),round(money*rate/12)])
    s += math.ceil(c)+round(money*rate/12)
    money -= math.ceil(c)
    list[i].append(s)

s += money + round(money*rate/12)
list.append([years,money,round(money*rate/12),s])     #最後一期的本金、利息、本利和

for j in range(years):     #輸出結果
    print("第" + str(list[j][0]) + "期", "本金（元）：" + str(list[j][1]), "利息（元）：" + str(list[j][2]), "本金利息累計（元）：" + str(list[j][3]))

    

