# Q2.2
![Question](images/Question.png)
### 設計一個隨機產生器 輸出在0到3

### 使用CRC8 來製作
##### 算式為 x^8 + x^2 + x +1
```verilog
assign temp = src[7] ^ src[1] ^ src[0];
```
```verilog
always@(posedge clk or posedge reset)begin
	if(reset)
```

##### 初始值(seed) 8'b10110101 取中間兩位做為輸出
```verilog
		src <= 8'b10110101;
	else if (signal)
		src <= {src[6:0] , temp};
end
```
![testbench](images/testbench.png)

![behavioral](images/behavioral.png)
##### 隨然取10個數中並沒有3 但在後續的模擬中是有的
![monitor](images/monitor.png)
