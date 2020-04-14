import pandas as pd
import numpy as np
import math

S = int(input('Stock Price:'))
u = float(input(':'))
d = float(input(':'))
r = float(input('rate:'))*0.01

R = math.exp(r)
p = (R-d)/(u-d)

X = int(input('Strike Price:'))
n = int(input('period:'))

stockprice = [[0]*n for i in range(n+1)]


for i in range(n+1):




