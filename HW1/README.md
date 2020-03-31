# HW1：本金平均攤還試算

*參考：https://ttc.scu.org.tw/memdca1.htm*  

## 學習歷程

1. 以前寫python都是用notepad++，這學期開始用visual studio code不太熟悉，在run的時候run不出來(可能是路徑的問題)，後來詢問同學之後解決了。  
2. 輸入本金用浮點數，跑的結果最後一期的本金和本利和會出現 .0：  
```
s += principle + round(principle*rate/12)
list.append([years,principle,round(principle*rate/12),s]) 
```
* Ex：輸入本金20萬、期數2年、年利率5%   
  `第24期 本金（元）：8318.0 利息（元）：35 本金利息累計（元）：210416.0`

後來在最後一期的結果把有本金的項目轉換為整數，最後輸出結果才正確。  
```
s += int(principle) + round(principle*rate/12)     #principle是浮點數，最後一期金額一定是整數因此用int
list.append([years,int(principle),round(principle*rate/12),s])
```
## 流程圖
![流程圖](https://github.com/a1999r71732/Financial_Engineering/blob/master/HW1/hw1%E6%B5%81%E7%A8%8B%E5%9C%96.png)
