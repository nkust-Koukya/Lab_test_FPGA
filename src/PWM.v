module pwm (clk , reset , signal , pwm);

input clk ,reset;
input [3:0] signal;
output reg pwm;

reg flag;
reg [3:0] current_state;  
reg [3:0] counter;  

always @(posedge clk or posedge reset) begin
    if (reset)begin
        counter <= 0;
        current_state <= 0;
        flag <= 0;
        end
    else if (counter == 9 || flag == 0)begin
        counter <= 0;
        current_state <= signal;
        flag <= 1;
        end 
    else 
        counter <= counter +1;
end

always @(*) begin
    if (counter < current_state)
        pwm = 1;
    else
        pwm = 0;
end

endmodule