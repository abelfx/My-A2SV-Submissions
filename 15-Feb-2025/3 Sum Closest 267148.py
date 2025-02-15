# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ == target:
                    return summ

                if abs(summ - target) < abs(result - target):
                    result = summ
                
                if summ > target:
                    right -= 1
                elif summ < target:
                    left += 1
            
        return result
                

