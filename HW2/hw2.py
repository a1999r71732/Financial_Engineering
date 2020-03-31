import numpy as np
import pandas as pd
import math

pv = float(input('Current Bond Price:'))   #現值 present value
f = float(input('Bond Par Value:'))   #票面價值par value
cr = float(input('coupon rate:'))   #coupon rate
years = int(input('years to maturity:'))   #到期年數
m = int(input('payment:'))   #一年複利幾次


p = m*years
c=(f*cr)/m*0.01

YTM=[0]*p

for i in range(p):
    total_pv=[pv*(-1)]+[c]*i+[c+f]
    YTM[i]=np.irr(total_pv)   #計算ytm


print("\nYTM: ", '%.3f' % (YTM[i]*100), "%")

#計算spotrate

t = int(input("Duration of spot rate(years):"))
print("Price of", str(t), "year unit zero-coupon bond:")
unitp = float(input())    #unitprice=pv/f

#SpotRate1 = (pv/f)**(-1/t) - 1    

SpotRate = (unitp)**(-1/t) - 1    

print(str(t),"year spot Rate of interst:", '%.2f' % (SpotRate*100), "%")

#forward rate


t1=int(input("Time due for the beginning of forward rate(years):"))
t2=int(input("Duration of forward rate(years):"))
time = t1+t2
print("Price of", str(t2),"year unit zero coupon bond:")
p1=float(input())
print("Price of", str(time),"year unit zero coupon bond:")
p2=float(input())

spotrate1 = (p1)**(-1/(t1))-1
spotrate2 = (p2)**(-1/(time))-1

F1 = ((1+spotrate2)**(time))/((1+spotrate1)**(t1))
forwardrate = ((F1**(1/t2))-1)*100

print(str(t2),"year forward rate of interest beginning ", str(t1),"years from now:",'%.2f' % (forwardrate), "%")

#forward rate對照表

allprice=[]

for i in range(time+1):
    print('Price of ',i,'year:')
    allprice.append(float(input()))

Forwardrate=[]

for i in range(time+1):
    list=[]
    for j in range(time+1):
        if i==j:
            list.append("0")
        elif i>j:
            list.append("x")
        else:
            if i==0:
                s=allprice[j]**(-1/j)-1 
                list.append(round(s,4))
            else:
                    f1=((allprice[i] / allprice[j]) ** (1 / j))-1
                    list.append(round(f1,4))

    Forwardrate.append(list)
Table = pd.DataFrame(Forwardrate)
print(Table)





