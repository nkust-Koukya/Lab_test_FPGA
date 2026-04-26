module testbench();
    reg clk , reset;
    reg [3:0] signal;
    wire pwm;
    
    pwm uut (clk , reset, signal, pwm);
    
    initial begin
        clk = 1;
        reset = 0;
    end
    
    initial begin
        #10 reset = 1;
        #10 reset = 0;
        
        signal = 2; 
        #100;
        
        signal = 9;
        #150
        
        signal = 5; 
        #200;
    
        signal = 8; 
        #200;
    end
        initial forever #10 clk = ~clk;
        initial #1500 $finish;

endmodule