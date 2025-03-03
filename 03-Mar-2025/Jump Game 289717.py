# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1

        i = len(nums) - 2
        while i >= 0:
            if i + nums[i] >= last_idx:
                last_idx = i
            i -= 1
        
        if last_idx == 0:
            return True
        return False