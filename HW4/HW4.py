import math
from scipy import stats

S = float(input('股票現價:'))
K = float(input('履約價:'))
d = float(input('股利:'))
sigma = float(input('波動率:'))
r = float(input('報酬率(%):'))*0.01
n = int(input('一年複息幾次:'))
M = float(input('剩餘到期日(年):'))



dividends = 0

for i in range(n):
    month = 1+3*i
    dividends += d*(math.exp(-r*(month/12)))

S_hat = S-dividends

d1 = (math.log(S_hat/K)+(r+(0.5)*sigma**2)*M)/((sigma)*math.sqrt(M))
d2 =  d1-(sigma)*math.sqrt(M)

call_p = S_hat*stats.norm.cdf(d1,0.0,1.0) - K*math.exp(-r*M)*stats.norm.cdf(d2,0.0,1.0)
put_p =  K*math.exp(-r*M)*stats.norm.cdf(-d2,0.0,1.0)-S_hat*stats.norm.cdf(-d1,0.0,1.0)

print('call option: '+'$',round(call_p,3))
print('put option: '+'$',round(put_p,3))
