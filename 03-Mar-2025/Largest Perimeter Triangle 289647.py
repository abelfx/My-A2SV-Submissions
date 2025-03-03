# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()

        maxx = float("-inf")
        for i in range(len(nums) - 2):
            if nums[i] + nums[i+1] > nums[i+2]:
                maxx = max(maxx,  nums[i] + nums[i+1] + nums[i+2])
        
        if maxx == float("-inf"):
            return 0
        
        return maxx


        