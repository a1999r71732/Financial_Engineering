# HW2：計算YTM、Spotrate、Forward rate
  

## 學習歷程

1. 首先計算YTM，本來想從上課交的公式推導出，用slove來解出未知的YTM。可是發現解不出來，所以另外找別的方法。 


![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/YTM%E5%85%AC%E5%BC%8F.png)


   從老師給的文章可知，YTM就是債券的內部報酬率，因此用numpy.irr可以計算出內部報酬率。下圖為internal return rate的計算公式
   
   
![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/irr.jpg)


2. 再計算Spotrate，利用公式:


![](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW2/spot.png)


3. 最後計算Forward rate

## 流程圖
![流程圖]()
