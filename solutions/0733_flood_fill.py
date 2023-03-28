"""
title : 0733_flood_fill.py
create : @tarickali 23/03/28
update : @tarickali 23/03/28
"""


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        def neighbors(
            image: list[list[int]], sr: int, sc: int
        ) -> list[tuple[int, int]]:
            N = []
            if sr + 1 < len(image):
                N.append((sr + 1, sc))
            if sr - 1 >= 0:
                N.append((sr - 1, sc))
            if sc + 1 < len(image[sr]):
                N.append((sr, sc + 1))
            if sc - 1 >= 0:
                N.append((sr, sc - 1))
            return N

        original_color = image[sr][sc]
        stack = [(sr, sc)]
        visited = {(sr, sc)}

        while len(stack) != 0:
            u = stack.pop()
            ur, uc = u
            for vr, vc in neighbors(image, ur, uc):
                if (vr, vc) not in visited and image[vr][vc] == original_color:
                    stack.append((vr, vc))
                    visited.add((vr, vc))
            image[ur][uc] = color
        return image
