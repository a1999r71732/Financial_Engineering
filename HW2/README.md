# HW2：計算YTM、Spotrate、Forward rate
  

## 學習歷程

1. 首先計算YTM，本來想從上課交的公式推導出，用slove來解出未知的YTM。可是發現解不出來，所以另外找別的方法。 


![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/YTM%E5%85%AC%E5%BC%8F.png)


   從老師給的文章可知，YTM就是債券的內部報酬率，因此用`numpy.irr`可以計算出內部報酬率。下圖為internal return rate的計算公式
   
   
![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/irr.jpg)

```
YTM[i]=np.irr(total_pv)
```


2. 再計算Spotrate，利用公式:


![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/spot.png)

零息債券計算公式是price=par value/(1+y<sub>t</sub>)<sup>n</sup>，所以價格除以票面價值就是unit zero coupon bond的價格。
本來想用這個方式計算:
```
SpotRate =(pv/f)**(-1/t) - 1    #pv是bond price，f是par value
```
為了和老師提供參考的計算器相同，再多輸入一個變數unitp代表單位零息債券的價格:
```
SpotRate =(unitp)**(-1/p) - 1 

```

3. 最後計算Forward rate
先輸入年數和Price算出spot rate，再用公式算出forward rate

![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/forwardrate.png)

再來處理表格，把表格下半部用x取代。

輸出結果:

*Price of  0 year:1
 Price of  1 year:0.95
 Price of  2 year:0.9
 Price of  3 year:0.8



```
   0       1       2       3
0  0  0.0526  0.0541  0.0772
1  x       0  0.0274   0.059
2  x       x       0    0.04
3  x       x       x       0
```

## 流程圖
![流程圖](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/HW2%E6%B5%81%E7%A8%8B%E5%9C%96.png)
