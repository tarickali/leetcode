"""
title : 0071_simplify_path.py
create : @tarickali 23/05/17
update : @tarickali 23/05/17
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for w in path.split("/"):
            if w == "." or w == "" or (w == ".." and len(stack) == 0):
                continue
            elif w == "..":  # and len(stack) > 0:
                stack.pop()
            else:
                stack.append(w)
        if len(stack) != 0 and stack[-1] == "":
            stack.pop()
        return "/" + "/".join(stack)
