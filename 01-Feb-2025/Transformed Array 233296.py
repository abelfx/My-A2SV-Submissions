# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length

        for i, a in enumerate(nums):
            result[i] = nums[(i + a) % length]

        return result