# Q2.2
![Question](images/Question.png)
### 設計一個隨機產生器 輸出在0到3
![code](images/code.png)
### 使用CRC8 來製作
##### 算式為 x^8 + x^2 + x +1
##### 初始值(seed) 8'b10110101 取中間兩位做為輸出
![testbench](images/testbench.png)

![behavioral](images/behavioral.png)
##### 隨然取10個數中並沒有3 但在後續的模擬中是有的
![monitor](images/monitor.png)
