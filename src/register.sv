module register (
  //signals
  input logic clk, reset,
  input logic write_ena,

  //in
  input logic [4:0] rs1, rs2, rs3,
  input logic [31:0] wd3,

  //out
  output logic [31:0] rd1, rd2);

  logic [31:0] rf [31:0];

  //sequential logic
  always_ff @ (posedge clk) begin
    if (reset) 
      rf <= '{default:32'b0};
    else if (write_ena)
      rf[rs3] <= wd3;
  end

  //combinational logic
  assign rd1 = rf[rs1];
  assign rd2 = rf[rs2];

endmodule

