class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            cur_min = val  # Defined inside 'if'
        else:
            cur_min = min(val, self.stack[-1][1])  # Defined inside 'else'
            
        # cur_min is fully accessible here because it lives in the function scope
        self.stack.append((val, cur_min))


    def pop(self) -> None:
        curval = self.stack.pop()
        minval = curval[1]
        self.minimum = minval

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
