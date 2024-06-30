"""
title : 0150_evaluate_reverse_polish_notation.py
create : @tarickali 23/06/13
update : @tarickali 23/06/13
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def compute(a: int, b: int, op: str) -> int:
            match op:
                case "+":
                    res = a + b
                case "-":
                    res = a - b
                case "*":
                    res = a * b
                case "/":
                    res = int(a / b)
            return res

        ops = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                c = compute(a, b, t)
                stack.append(c)
        return stack[-1]
