# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        # k = 3 % 7
        temp = nums[-k:]
        # temp = [5,6,7]
        nums[k:] = nums[:-k]
        # [4, 5, 6, 7] = [1, 2, 3, 4] 
        nums[:k] = temp        
        # [1, 2, 3] = [5, 6, 7]

        