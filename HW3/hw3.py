import pandas as pd
import numpy as np
import math

S = int(input('Stock Price:'))
u = float(input('growth:'))
d = float(input('regress:'))
r = float(input('rate:'))*0.01

R = math.exp(r)
p = (R-d)/(u-d)


X = int(input('Strike Price:'))
n = int(input('period:'))

stockprice = [[0]*(n+1) for i in range(n+1)]

stockprice[0][0] = S

for i in range(1,n+1):                #紀錄stock price
    for j in range(n+1):
        if i == j:
            stockprice[i][j]=stockprice[i-1][j-1]*d

        else:
            stockprice[i][j]=stockprice[i-1][j]*u

callp = [[0]*(n+1) for i in range(n+1)]

for i in range(0,n+1):             #算出每一層的call price
    if stockprice[n][i]-X  >0:
        callp[n][i]=stockprice[n][i]-X

for i in range(0,n):
    for j in range(0,n):
        callp[n-1-i][j]=round((callp[n-i][j]*p + callp[n-i][j+1]*(1-p))/R,3)

callp[0][1]=0

putp = [[0]*(n+1) for i in range(n+1)]

for i in range(0,n+1):            #算出每一層的put price
    if X-stockprice[n][i]  >0:
        putp[n][i]=X-stockprice[n][i]

for i in range(0,n):
    for j in range(1,n+1):
        putp[n-1-i][j]=round((putp[n-i][j-1]*p + putp[n-i][j]*(1-p))/R,3)


print('call value:', callp[0][0])
print('put value:' , putp[0][n])

