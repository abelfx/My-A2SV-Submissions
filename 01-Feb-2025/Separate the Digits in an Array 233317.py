# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lst = []

        for i in range(len(nums)):
            for j in str(nums[i]):
                lst.append(j)

        lstF = []
        for i in lst:
            lstF.append(int(i))

        return lstF

