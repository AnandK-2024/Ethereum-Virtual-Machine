import imp
from typing import Counter


import Memory
import Stack
import Memory
class ExecutionContext:
    # @parameters pragramming Counter
    def __init__(self, code=bytes(),pc=0, memory=Memory(),stack=Stack()):
        self.Code=code
        self.pc=pc
        self.memory=memory
        self.stack=stack
        self.stopped=False

    def stop(self):
        self.stopped=True

    def read_code(self, num_bytes):
        value=int.from_bytes(self.Code[self.pc:self.pc+num_bytes],byteorder="big")
        self.pc+=num_bytes
        return value