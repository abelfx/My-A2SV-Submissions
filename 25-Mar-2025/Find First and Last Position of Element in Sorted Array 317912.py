# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.first_position = -1
        self.last_position = -1

        def first_position(l, r):
            while l <= r:
                mid = (l + r)//2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if nums[mid] == target:
                        self.first_position = mid
                    r = mid - 1
        
        def last_position(l, r):
            while l <= r:
                mid = (l + r)//2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[mid] == target:
                        self.last_position = mid
                    l = mid + 1
        
        first_position(0, len(nums)-1)
        last_position(0, len(nums)-1)

        return [self.first_position, self.last_position]
                
        

        

        