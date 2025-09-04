module alu_basic (
    input logic [31:0] src1, src2,
    input logic [2:0] sel_alu,

    output logic [31:0] result
);

    always_comb begin
        case (sel_alu)
            // ADD
            3'b000 : result = src1 + src2; 
            // SUB...add src1 to the 2's complement of src2
            3'b001 : result = src1 + (~src2 + 1'b1); 
            // AND...use & instead of && for bitwise operation
            3'b010 : result = src1 & src2; 
            // OR...use | instead of || for bitwise operation
            3'b011 : result = src1 | src2; 
            // XOR
            3'b100 : result = src1 ^ src2; 
            default : result = 32'b0;
        endcase
    end

endmodule