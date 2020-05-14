# HW4：Black-Scholes model
  

## 學習歷程

#### 1. 將股票現價、履約價、股利、波動率、報酬率、期數和到期日輸入
```
S = float(input('股票現價:'))
K = float(input('履約價:'))
d = float(input('股利:'))
sigma = float(input('波動率:'))
r = float(input('報酬率(%):'))*0.01
n = int(input('一年複息幾次:'))
M = float(input('剩餘到期日(年):'))
```
測資:
```
股票現價:75
履約價:65 
股利:1 
波動率:0.35 
報酬率(%):6 
一年複息幾次:2 
剩餘到期日(年):0.5 
```
***
#### 2. 計算總共會付多少股利

```
for i in range(n):
    month = 1+3*i
    dividends += d*(math.exp(-r*(month/12)))
```
輸出結果:
```
1.9752111524994376
```
***
#### 3. 將Black Scholes model中的S代換成 *S_hat=S-D*，計算d1、d2

```
S_hat = S-dividends

d1 = (math.log(S_hat/K)+(r+(0.5)*sigma**2)*M)/((sigma)*math.sqrt(M))
d2 =  d1-(sigma)*math.sqrt(M)
```
***
#### 4. 計算call option和put option並輸出
```
call_p = S_hat*stats.norm.cdf(d1,0.0,1.0) - K*math.exp(-r*M)*stats.norm.cdf(d2,0.0,1.0)
put_p =  K*math.exp(-r*M)*stats.norm.cdf(-d2,0.0,1.0)-S_hat*stats.norm.cdf(-d1,0.0,1.0)

print('call option: '+'$',round(call_p,3))
print('put option: '+'$',round(put_p,3))
```
輸出結果:
```
call option: $ 12.806
put option: $ 2.86
```
## 流程圖
![流程圖](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW4/%E6%B5%81%E7%A8%8B%E5%9C%96.png)
