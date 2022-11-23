class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        memo = [0] * n
        memo[0], memo[1] = cost[0], cost[1] 
        for i in range(2, n):
            memo[i] = min(memo[i-1], memo[i-2]) + cost[i]
        return min(memo[n-1], memo[n-2])
