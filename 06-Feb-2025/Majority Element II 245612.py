# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)


        lst = []
        for keys, values in count.items():
            if (values > len(nums)/3):
                lst.append(keys)

        
        return lst