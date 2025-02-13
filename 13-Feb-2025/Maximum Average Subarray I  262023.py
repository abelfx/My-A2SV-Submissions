# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_total = 0

        for i in range(k):
            current_total += nums[i]
        
        max_ave = current_total/k

        for i in range(k, len(nums)):
            current_total -= nums[i-k]
            current_total += nums[i]
            max_ave = max(max_ave, current_total/k)
        
        return max_ave
        
        
        