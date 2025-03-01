# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxx = float("-inf")
        minn = float("inf")

        curr_max = 0
        cur_min = 0

        for num in nums:
            curr_max = max(num, curr_max + num)
            maxx = max(maxx, curr_max)
        
        for num in nums:
            cur_min = min(num, cur_min + num)
            minn = min(minn, cur_min)
        
        if abs(maxx) > abs(minn):
            return abs(maxx)
        else:
            return abs(minn)