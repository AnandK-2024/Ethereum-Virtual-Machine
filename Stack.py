from Exception import StackOverFlow, InvalidStackItem
# The EVM is a simple stack-based architecture.


class Stack:

    # . The stack has a maximum size of 1024
    def __init__(self, max_depth=1024):
        self.stack = []
        self.max_depth = max_depth

    def push(self, item: int):
        #  The word size of the machine (and thus size of stack items) is 256-bit
        if (item < 0 or item > 2**256-1):
            raise InvalidStackItem({"item": item})

        # Stack Overflow occurs when you are trying to call function recursively
        # and there is no condition to stop it, in solidity stack can be at most 1024 frame,
        #  so a function can call itself only 1024x times, if you exceed that stack Overflow will occur.
        elif (len(self.stack)+1 > self.max_depth):
            raise StackOverFlow()

        else:
            self.stack.append(item)
