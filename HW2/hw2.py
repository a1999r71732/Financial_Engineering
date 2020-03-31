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


SpotRate = math.pow(pv/f, -1/p) - 1    #計算spotrate





print("\nYTM: ", '%.3f' % (YTM[i]*100), "%")
print("\nSpot Rate: ", '%.3f' % (SpotRate*100), "%")


