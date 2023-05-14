"""
title : 0735_asteroid_collision.py
create : @tarickali 23/05/14
update : @tarickali 23/05/14
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        i = 0

        while i < len(asteroids):
            curr = asteroids[i]
            if len(stack) == 0 or int(curr > 0) >= int(stack[-1] > 0):
                stack.append(curr)
                i += 1
            elif abs(curr) > abs(stack[-1]):
                stack.pop()
            elif abs(curr) == abs(stack[-1]):
                stack.pop()
                i += 1
            else:
                i += 1
        return stack
