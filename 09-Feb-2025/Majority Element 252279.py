# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for keys, values in count.items():
            if (values > len(nums)/2):
                return keys

        
        return 0
        