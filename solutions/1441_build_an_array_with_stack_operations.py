"""
title : 1441_build_an_array_with_stack_operations.py
create : @tarickali 23/11/03
update : @tarickali 23/11/03
"""


class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        operations = []
        stack = []
        k = 0
        for i in range(1, n + 1):
            if stack == target:
                break

            stack.append(i)
            operations.append("Push")

            if target[k] != stack[-1]:
                stack.pop()
                operations.append("Pop")
            else:
                k += 1

        return operations
