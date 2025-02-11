# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []

        nums.sort()
        
        for indx, val in enumerate(nums):
            if val == target:
                result.append(indx)
        
        return result
        