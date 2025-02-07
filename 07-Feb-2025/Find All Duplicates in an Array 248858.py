# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict = Counter(nums)

        result = []
        for keys, values in dict.items():
            if(values == 2):
                result.append(keys)

        return result