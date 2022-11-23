class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        T = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in T:
                return [i, T[y]]
            T[x] = i
        return [None, None]
