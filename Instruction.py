from base64 import decode
from Exception import NonImplimentedError, InvalideCodeOffset,UnknownOpcode
from multiprocessing import context
import opcode
import ExecutionContext

INSTRUCTIONS = []
INSTRUCTIONS_BY_OPCODE = {}


class Instruction:
    def __init__(self, opcode: int, name: str):
        self.opcode = opcode
        self.name = name

    def execute(self, context: ExecutionContext):
        raise NonImplimentedError()

    def register_instruction(opcode: int, name: str, execute_fun: callable):
        instruction = Instruction(opcode, name)
        instruction.execute = execute_fun
        INSTRUCTIONS.append(instruction)

        assert opcode not in INSTRUCTIONS_BY_OPCODE
        INSTRUCTIONS_BY_OPCODE[opcode] = instruction
        return instruction

    def decode_opcode(self,Context: ExecutionContext):
        if (context.pc <0 or context.pc>=len(context.code)):
            raise InvalideCodeOffset({"code":context.code,"pc":context.pc})
        opcode=context.read_code(1)
        instruction=INSTRUCTIONS_BY_OPCODE.get(opcode)
        if instruction is None:
            raise UnknownOpcode({"opcode":opcode})
        return instruction

    def run(self,code:bytes):
        context=ExecutionContext(code=code)
        while not context.stopped:
            pc_before=context.pc
            instruction=self.decode_opcode(context)
            self.execute(context)
            print(f"{instruction}@ pc={pc_before}")
            print(context)
            print()

    STOP = register_instruction(0x00, "STOP", (lambda ctx: ctx.stop()))

    PUSH1 = register_instruction(0x01, "PUSH1", (lambda ctx: ctx.push(ctx.read_code(1))))

    ADD= register_instruction(0x01, "ADD", (lambda ctx: ctx.push(
        (ctx.stack.pop()+ctx.stake.pop()) % 2**256)))

    MUL = register_instruction(0x02, "MUL", (lambda ctx: ctx.push(
        (ctx.stack.pop()*ctx.stake.pop()) % 2**256)))
