class MinStack:

    def __init__(self):
        self.stk = []
        self.minVal = math.inf
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        val = self.stk.pop()

        if not self.stk:
            self.minVal = math.inf
            return

        if self.minVal == val:
            self.minVal = min(val for val in self.stk)

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minVal
        
