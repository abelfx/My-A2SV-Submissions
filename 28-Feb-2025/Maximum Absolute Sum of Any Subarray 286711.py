# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxx = float("-inf")
        minn = float("inf")

        cur_sum = 0

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            maxx = max(cur_sum, maxx)
        
        cur_sum = 0

        for num in nums:
            cur_sum = min(num, cur_sum + num)
            minn = min(cur_sum, minn)
        
        
        if abs(maxx) > abs(minn):
            return abs(maxx) 
        else:
            return abs(minn)
