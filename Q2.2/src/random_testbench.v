`timescale 1ns / 1ps
module testbench();
    reg clk , reset ,signal;
    wire [1:0] num;

    random uut(clk , reset, signal, num);

	initial begin
		clk = 0;
		reset = 0;
		signal = 0;
	end
	integer i;
	initial begin
		#10 reset = 1;
		#10 reset = 0;
        #10 signal = 1;
        
    
    for (i = 0; i < 10; i = i + 1) begin
        #20;
        $display("Random = %d", num);
    end
end

    initial forever #10 clk = ~clk;
    initial #1500 $finish;
endmodule