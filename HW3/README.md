# HW3：Binomoal Option Pricing Model
  

## 學習歷程

#### 1.先輸入起始值

#### 2.根據老師上課的公式，先計算出在Binomial tree裡會出現的所有stock price，然後用二維陣列表示。

```
for i in range(1,n+1):               
    for j in range(n+1):
        if i == j:
            stockprice[i][j]=stockprice[i-1][j-1]*d

        else:
            stockprice[i][j]=stockprice[i-1][j]*u
print(stockprice)
```
輸出結果:
```
[[160, 0, 0, 0], 
[240.0, 80.0, 0.0, 0.0],
[360.0, 120.0, 40.0, 0.0],
[540.0, 180.0, 60.0, 20.0]]
```

#### 3.計算每個call price，也利用老師上課的公式。

```
callp = [[0]*(n+1) for i in range(n+1)]

for i in range(0,n+1):            
    if stockprice[n][i]-X  >0:
        callp[n][i]=stockprice[n][i]-X

for i in range(0,n):
    for j in range(0,n):
        callp[n-1-i][j]=round((callp[n-i][j]*p + callp[n-i][j+1]*(1-p))/R,3)

callp[0][1]=0
print(callp)
```

輸出結果:
```
[[85.069, 0, 0.0, 0], 
[141.458, 10.208, 0.0, 0], 
[235.0, 17.5, 0.0, 0], 
[390.0, 30.0, 0, 0]]
```

#### 4.計算每個put price，方法跟call price一樣。

```
putp = [[0]*(n+1) for i in range(n+1)]

for i in range(0,n+1):            #算出每一層的put price
    if X-stockprice[n][i]  >0:
        putp[n][i]=X-stockprice[n][i]

for i in range(0,n):
    for j in range(1,n+1):
        putp[n-1-i][j]=round((putp[n-i][j-1]*p + putp[n-i][j]*(1-p))/R,3)
print(putp)
```

輸出結果:
```
[[0, 0.0, 1.406, 11.875], 
[0, 0.0, 5.625, 34.375],
[0, 0.0, 22.5, 85.0], 
[0, 0, 90.0, 130.0]]
```
#### 5.輸出最後推回的值

```
print('call value:', callp[0][0])
print('put value:' , putp[0][n])
```

輸出結果:
```
call value: 85.069
put value: 11.875
```
## 流程圖
![流程圖](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW3/hw3%E6%B5%81%E7%A8%8B%E5%9C%96.png)
