`timescale 1ns / 1ps
module trafficLight_testbench( );
	reg  clk, reset ; 
	wire [1:0] light;
	
	trafficlight  uut (clk, reset , light);
	
	initial begin
		clk = 0;
		reset = 0;
	end
	
	initial begin
		#10 reset = 1;
		#10 reset = 0;
	end
	
	initial forever #10 clk = ~clk;
	initial $monitor($time, " light = %b", light);
	initial #1000 $finish;
	
		
endmodule
