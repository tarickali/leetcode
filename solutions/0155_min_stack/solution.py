"""
title : 0155_min_stack.py
create : @tarickali 23/05/17
update : @tarickali 23/05/17
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minval = float("inf")

    def push(self, val: int) -> None:
        self.stack.append((val, self.minval))
        if val < self.minval:
            self.minval = val

    def pop(self) -> None:
        val, minval = self.stack.pop()
        self.minval = minval

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
