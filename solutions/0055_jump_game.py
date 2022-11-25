class Solution:
    def canJump(self, nums: list[int]) -> bool: 
        n = len(nums)
        dest = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= dest: dest = i
            else: dest = max(dest, i + nums[i])
        return dest == 0
