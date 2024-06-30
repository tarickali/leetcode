"""
title : 0074_search_a_2d_matrix.py
create : @tarickali 23/06/12
update : @tarickali 23/06/12
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        trow, brow = 0, len(matrix)
        lcol, rcol = 0, len(matrix[0])

        while trow < brow and lcol < rcol:
            mrow = trow + (brow - trow) // 2
            mcol = lcol + (rcol - lcol) // 2

            if matrix[mrow][mcol] == target:
                return True
            elif matrix[mrow][mcol] > target:
                if matrix[mrow][0] > target:
                    brow = mrow
                else:
                    rcol = mcol
            else:  # matrix[mrow][mcol] < target
                if matrix[mrow][-1] < target:
                    trow = mrow + 1
                else:
                    lcol = mcol + 1

        return False
