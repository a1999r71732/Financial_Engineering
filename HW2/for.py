#forward rate
import pandas as pd

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