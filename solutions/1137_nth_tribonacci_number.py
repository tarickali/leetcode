class Solution:
    def tribonacci(self, n: int) -> int:
        # Dynamic programming with no memoization
        if n < 3: return n if n < 2 else n - 1
        a, b, c, d = 0, 1, 1, 2
        for _ in range(3, n+1):
            d = a + b + c
            a, b, c = b, c, d
        return d
    
    def tribonacci(self, n: int) -> int:
        # Dynamic programming with memoization
        memo = [0, 1, 1]
        for i in range(3, n+1):
            memo.append(memo[i-1] + memo[i-2] + memo[i-3])
        return memo[n]

    def tribonacci(self, n: int) -> int:
        # Recursive algorithm
        if n < 3: return n if n < 2 else n - 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)