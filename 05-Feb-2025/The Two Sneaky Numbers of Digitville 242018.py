# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dict = Counter(nums)

        lst = []
        for keys, values in dict.items():
            if values == 2:
                lst.append(keys)
        
        return lst
        