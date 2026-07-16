class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            topElement = float('inf')
        else:
            topElement = self.minStack[len(self.minStack) - 1]
        self.minStack.append(min(topElement, val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
        
