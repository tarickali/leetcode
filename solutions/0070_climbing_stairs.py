'''
title : 0070_climbing_stairs.py
create : @tarickali 23/11/22
update : @tarickali 23/11/22
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0], memo[1] = 1, 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
