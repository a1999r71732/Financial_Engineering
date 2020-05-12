# HW5：Option Pricing with Hull White Model
  

## 學習歷程

#### 1.先輸入起始值

```
sigma=0.1
a=0.2
timestep:1200
length(year):1
forward rate(%):3
current stock price:100
exercise price:105
risk-free interest rate(%):1

```

#### 2.套入QuantLib套件，模擬short rate

```
num_paths = 1000

day_count = ql.Thirty360()
todays_date = ql.Date(13, 5, 2020)

ql.Settings.instance().evaluationDate = todays_date

spot_curve = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)

hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, T, timestep, rng, False)

def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr


time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()
```
輸出結果:

![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW5/Figure_1.png)

#### 3.再帶入GBM，模擬股價

```
def genBrownMotion(T,mu,sigma,S0,dt):
    n = round(T/dt)
    t = np.linspace(0, T,n+1)
    W = [0]+np.random.standard_normal(size = timestep+1)
    W = np.cumsum(W)*np.sqrt(dt)
    X = (mu-0.5*sigma**2)*t+sigma*W
    S= S0*np.exp(X)
    plt.plot(t,S)
    return S

S_path=[]

for i in range(0,num_paths):
    S_path.append(genBrownMotion(T,paths[i],sigma,S0,dt))

plt.title("GBM for Stock price")
plt.show()

```

輸出結果:

![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW5/GBM.png)


#### 4.計算call price和put price期望值，折現至第一期
```
Call_p = []
Put_p = []

for i in range(num_paths):
    Call_p.append(max(0,S_path[i][-1]-K))
    Put_p.append(max(0,K-S_path[i][-1]))

Call_Price = np.mean(Call_p)*np.exp(-timestep*r)
Put_Price = np.mean(Put_p)*np.exp(-timestep*r)

print("Call Price:", Call_Price)
print("Put Price:", Put_Price)
```

輸出結果:
```
Call Price: 7.84509158880052e-05
Put Price: 6.215232677376142e-05
```
## 流程圖
![流程圖](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW5/%E6%B5%81%E7%A8%8B%E5%9C%96.png)
