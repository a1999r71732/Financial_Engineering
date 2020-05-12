import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np

sigma = float(input("sigma:"))
a = float(input("a:"))
timestep = int(input("timestep:"))
T = int(input("length(year):")) # in years
forward_rate = float(input("forward rate(%):"))*0.01

S0 = float(input("current stock price:"))
K = float(input("exercise price:"))
r = float(input("risk-free interest rate(%):"))*0.01


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


dt = T/timestep

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

Call_p = []
Put_p = []

for i in range(num_paths):
    Call_p.append(max(0,S_path[i][-1]-K))
    Put_p.append(max(0,K-S_path[i][-1]))

Call_Price = np.mean(Call_p)*np.exp(-timestep*r)
Put_Price = np.mean(Put_p)*np.exp(-timestep*r)

print("Call Price:", Call_Price)
print("Put Price:", Put_Price)