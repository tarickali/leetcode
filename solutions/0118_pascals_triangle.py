"""
title : 0118_pascals_triangle.py
create : @tarickali 23/03/08
update : @tarickali 23/03/08
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangles = [[] for _ in range(numRows)]
        def recurse(n: int) -> None:
            if n == 1:
                triangles[n-1] = [1]
            else:
                recurse(n-1)
                triangles[n-1] = [1]
                for i in range(1, n-1):
                    triangles[n-1].append(triangles[n-2][i-1] + triangles[n-2][i])
                triangles[n-1].append(1)

        recurse(numRows)
        return triangles

