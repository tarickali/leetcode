'''
title : 0055_jump_game.py
create : @tarickali 25/11/23
update : @tarickali 27/11/23
'''

class Solution:
    def canJump(self, nums: list[int]) -> bool: 
        n = len(nums)
        dest = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= dest: dest = i
        return dest == 0

    # def canJump(self, nums: list[int]) -> bool: 
    #     best = 0
    #     for i, n in enumerate(nums):
    #         if i > best: return False
    #         best = max(best, i + n)
    #     return best >= len(nums) - 1
