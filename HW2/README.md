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

零息債券計算公式是price=par value/(1+y<sub>t</sub>)<sup>n</sup>，所以價格除以票面價值就是unit zero coupon bond，因此套用公式:

```
SpotRate =(pv/f)**(-1/p) - 1    #pv是bond price，f是par value，p是年數乘上一年期數
```

3. 最後計算Forward rate

## 流程圖
![流程圖](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/HW2%E6%B5%81%E7%A8%8B%E5%9C%96.png)
