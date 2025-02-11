# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if(int(str(nums[j]) + str(nums[j+1])) < int(str(nums[j+1]) + str(nums[j]) )):
                   temp = nums[j]
                   nums[j] = nums[j+1]
                   nums[j+1] = temp

        result = ""
        for i in nums:
            result += str(i)
        
        return str(int(result))
                   