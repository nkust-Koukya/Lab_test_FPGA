module trafficlight(clk, reset , light);// green 8clk yellow 2clk red 10clk
input clk , reset;
output reg [1:0] light;

parameter state_close  = 2'd0,
		  state_red    = 2'd1,
		  state_green  = 2'd2,
		  state_yellow = 2'd3;

parameter red 	 = 2'd0,
		  green  = 2'd1,
		  yellow = 2'd2,
		  close  = 2'd3;

reg [1:0] current_state , next_state , timer_yellow;
reg [3:0] timer_green;
reg [4:0] timer_red;

always@(posedge clk or posedge reset)begin// reset
	if(reset) current_state <= state_close;
	else current_state <= next_state;
end

always@(posedge clk)begin
	case(current_state)
	state_close: begin
                timer_red <= 0;
                timer_green <= 0;
                timer_yellow <= 0;
            end
	state_red:begin
				timer_red <= timer_red + 1; 
				timer_green <= 0 ;
				timer_yellow <= 0;
		   end
	state_green:begin
				timer_green <= timer_green + 1;
				timer_yellow <= 0; 
				timer_red <= 0;
		end
	state_yellow:begin
				timer_yellow <= timer_yellow + 1 ;
				timer_red <= 0 ;
				timer_green <= 0;
		end
	endcase
end

always@(*)begin//current_state
	case(current_state)
	state_close: next_state = state_red;
	state_red  : next_state =(timer_red == 9)? state_green : state_red;
	state_green: next_state =(timer_green == 7)? state_yellow : state_green;
	state_yellow:next_state =(timer_yellow == 1)? state_red : state_yellow;
	endcase
end

always@(*)begin//light
	case(current_state)
	state_close: light = close;
	state_red  : light = red;
	state_green: light = green;
	state_yellow:light = yellow;
	endcase
end
endmodule