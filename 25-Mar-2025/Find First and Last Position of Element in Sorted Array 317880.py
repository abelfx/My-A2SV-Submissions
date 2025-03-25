# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = -1
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        l = first
        r = first
        checkerR = True
        checkerL = True
        
        while checkerL or checkerR:
            if l > 0 and checkerL and nums[l-1] == target:
                l = l-1
            else:
                checkerL = False

            if r < len(nums) - 1 and checkerR and nums[r+1] == target:
                r = r+1
            else:
                checkerR = False

        
        return [l, r]

        

        