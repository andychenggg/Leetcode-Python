from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mono_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mono_stack) == 0 or self.mono_stack[-1] >= val:
            self.mono_stack.append(val)

    def pop(self) -> None:
        e = self.stack.pop()
        if e==self.mono_stack[-1]:
            self.mono_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mono_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()