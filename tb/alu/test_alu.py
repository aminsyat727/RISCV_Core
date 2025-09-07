import cocotb
from cocotb.triggers import Timer
import random

## test ADD
@cocotb.test()
async def ADD_test(dut):
    await Timer(1, units="ns")
    dut.sel_alu.value = 0b000
    for _ in range(1000):
        src1 = random.randint(0x00000000,0xFFFFFFFF)
        src2 = random.randint(0x00000000,0xFFFFFFFF)
        dut.src1.value = src1
        dut.src2.value = src2
        # We mask expected to not take account of overflows
        expected = (src1 + src2) & 0xFFFFFFFF
        # Await 1 ns for the infos to propagate
        await Timer(1, units="ns")
        assert int(dut.result.value) == expected

##test AND
@cocotb.test()
async def AND_test(dut):
    await Timer(1, units="ns")
    dut.sel_alu.value = 0b010
    for _ in range(1000):
        src1 = random.randint(0x00000000,0xFFFFFFFF)
        src2 = random.randint(0x00000000,0xFFFFFFFF)
        dut.src1.value = src1
        dut.src2.value = src2
        expected = src1 & src2
        # Await 1 ns for the infos to propagate
        await Timer(1, units="ns")
        assert int(dut.result.value) == expected       

#test OR
@cocotb.test()
async def OR_test(dut):
    await Timer(1, units="ns")
    dut.sel_alu.value = 0b011
    for _ in range(1000):
        src1 = random.randint(0x00000000,0xFFFFFFFF)
        src2 = random.randint(0x00000000,0xFFFFFFFF)
        dut.src1.value = src1
        dut.src2.value = src2
        expected = src1 | src2
        # Await 1 ns for the infos to propagate
        await Timer(1, units="ns")
        assert int(dut.result.value) == expected   

##test XOR
@cocotb.test()
async def XOR_test(dut):
    await Timer(1, units="ns")
    dut.sel_alu.value = 0b100 #xor
    for _ in range(1000):
        src1 = random.randint(0x00000000,0xFFFFFFFF)
        src2 = random.randint(0x00000000,0xFFFFFFFF)
        dut.src1.value = src1
        dut.src2.value = src2

        await Timer(1, units="ns")
        expected = src1 ^ src2

        assert int(dut.result.value) ==  int(expected)