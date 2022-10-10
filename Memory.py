from Exception import InvalidMemoryAccess, InvalidMemoryValue
# The memory model is a simple word-addressed byte array
# memory is volatile

MAX_UINT256=2**256-1
class Memory:
    def __init__(self):
        self.memory=[]
    
    def store(self, offset:int, value:int):
        if offset<0 or offset>MAX_UINT256:
            raise InvalidMemoryAccess({"offset":offset,"value":value})

        elif(value<0 or value>MAX_UINT256):
            raise InvalidMemoryValue({"offset":offset,"value":value})

        # expand memory if nessasery
        elif(offset>=len(self.memory)):

            # intialize with 0x00   
            self.memory.extend([0]*offset-len(self.memory)+1)

        self.memory[offset]=value

    def load(self, offset:int):
        if (offset<0):
            raise InvalidMemoryAccess({"offset": offset})
        elif(offset>=len(self.memory)):
            return 0
        else:
            return self.memory[offset]
        
