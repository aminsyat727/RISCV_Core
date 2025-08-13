# RISCV_Core
RISC-V Core personal design project using RV32I base instruction sets  

# SINGLE CYCLE CORE  
A simple single cycle core consist of a datapath and a control unit.  

## Datapath 
The "Engine" of the processor, handling data in and out and processing it.   
1. Program Counter
2. Memory (Instruction and Data)
3. Register
4. ALU
5. Sign Extender

## Control Unit  
The "Controller" of the datapath. Determines what to be executed, which data or path to be taken and regulate the data flow.  
1. Main Decoder
2. ALU Decoder


## RV32I instruction sets  
<img width="594" height="700" alt="image" src="https://github.com/user-attachments/assets/f0a7fa76-1cd4-4c4b-8bfd-99f25e581234" />
