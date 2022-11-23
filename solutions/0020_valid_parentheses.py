class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in brackets: # c is either (, {, or [
                stack.append(c)
            else: # c is either ), }, ]
                if len(stack) == 0: return False
                elif stack[-1] != brackets[c]: return False
                else: stack.pop()
        return len(stack) == 0