# [15-8-2025]  
## RV32I Overview

### Instruction Set Summary
- **40 unique instructions** (can be reduced to 38 if `FENCE = NOP` and `ECALL`/`BREAK` share encoding)
- **32 registers** (`x0` hardwired to zero; `x1`–`x31` general-purpose)
- **Program Counter (PC)** holds address of the current instruction
- **6 formats**: R, I, S, U, B (S-variant), J (U-variant)
- **All instructions are 32 bits**
- Misaligned branch/jump targets cause exceptions

---

### Instruction Formats
- **Core**: R / I / S / U
- **Additional**:  
  - **B-type**: like S-type but different immediate positions  
  - **J-type**: like U-type but different immediate positions

---

### Arithmetic & Logic
- **I-type (reg-imm)**: `ADDI`, `SLTI`, `SLTIU`, `ANDI`, `ORI`, `XORI`, `SLLI`, `SRLI`, `SRAI`
- **U-type**: `LUI`, `AUIPC` (load/add to PC)
- **R-type (reg-reg)**: `ADD`, `SUB`, `SLT`, `SLTU`, `AND`, `OR`, `XOR`, `SLL`, `SRA`, `SRL`

---

### NOP
- Advances PC, sync, or leaves space for inline mods
- Encoded as: `ADDI x0, x0, 0`

---

### Control Transfer
#### Unconditional Jumps
- **`JAL`** (J-type): `(PC + 4)` → `rd`
- **`JALR`** (I-type)

#### Conditional Branches (B-type)
- `BEQ` / `BNE`: branch if equal / not equal
- `BLT` / `BLTU`: branch if `<` (signed/unsigned)
- `BGE` / `BGEU`: branch if `>=` (signed/unsigned)

---

### Memory Operations
#### LOAD (I-type, mem → reg)
- `LW` (32-bit)  
- `LH` / `LHU` (16-bit, sign/zero-extend)  
- `LB` / `LBU` (8-bit, sign/zero-extend)

#### STORE (S-type, reg → mem)
- `SW` (32-bit)  
- `SH` (16-bit)  
- `SB` (8-bit)

---

### Memory Ordering
- For sync: `FENCE`, `FENCE.TSO`

---

### System Instructions
- **`ECALL`**: request service from environment
- **`EBREAK`**: return control to debugger
- **Hints**: like `NOP`, may be used for sync or PC advance


# [14-8-2025]  
**Read on RISC-V Introduction**  
- RISC-V (pronounced “risk-five”)   
- Each base integer instruction set is characterized by the width of the integer registers and the corresponding size of the address space and by the number of integer registers.  
- 2 primary base integer: RV3I and RV64
- References: https://five-embeddev.com/riscv-user-isa-manual/Priv-v1.12/intro.html#introduction
