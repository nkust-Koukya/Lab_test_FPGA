module random (clk, reset, signal , num);
input clk, reset, signal;
output [1:0] num;

reg [7:0] src;
wire temp;

assign temp = src[7] ^ src[1] ^ src[0];

always@(posedge clk or posedge reset)begin
	if(reset)
		src <= 8'b10110101;
	else if (signal)
		src <= {src[6:0] , temp};
end

assign num = src[5:4];

endmodule
