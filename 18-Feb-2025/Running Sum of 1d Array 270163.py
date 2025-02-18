# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            nums[i] = prefix_sum
        
        return nums