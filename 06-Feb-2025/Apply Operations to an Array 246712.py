# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] == nums[j]:
                nums[i] = nums[i]  * 2
                nums[j] = 0
       
        return [x for x in nums if x != 0] + [x for x in nums if x == 0]