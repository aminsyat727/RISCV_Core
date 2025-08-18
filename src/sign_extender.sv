module sign_extender (
    input logic [31:0] inst,
    input  logic [2:0] sel_imm,
    output  logic [31:0] immediate
);

always_comb begin
    case (sel_imm)
        // I Type 
        3'b000  : immediate = {{20{inst[31]}}, inst[31:20]};
        // S Type 
        3'b001  : immediate = {{20{inst[31]}}, inst[31:25], inst[11:7]};
        // B Type 
        3'b010  : immediate = {{19{inst[31]}}, inst[31], inst[7], inst[30:25], inst[11:8], 1'b0};
        // U Type 
        3'b011  : immediate = {{inst[31:12]}, 12'h000};
        // J Type 
        3'b100  : immediate = {{11{inst[31]}}, inst[31], inst[19:12], inst[20], inst[30:21], 1'b0};
        default : immediate = 32'h00000000;
    endcase
end

endmodule

