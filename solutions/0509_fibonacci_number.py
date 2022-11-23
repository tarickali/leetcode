class Solution:
    def fib(self, n: int) -> int:
        # Dynamic programming with no memoization
        if n < 2: return n
        a, b, c = 0, 1, 1
        for _ in range(2, n+1):
            c = a + b
            a, b = b, c
        return c

    # def fib(self, n: int) -> int:
    #     # Dynamic programming with memoization
    #     memo = [0, 1]
    #     for i in range(2, n+1):
    #         memo.append(memo[i-1] + memo[i-2])
    #     return memo[n]
    
    # def fib(self, n: int) -> int:
    #     # Recursive algorithm
    #     if n < 2: return
    #     return self.fib(n-1) + self.fib(n-2)
