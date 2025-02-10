# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums) == 1): return nums

        mid = len(nums) // 2
        left_lst = self.sortArray(nums[:mid])
        right_lst = self.sortArray(nums[mid:])

        return self.mergerList(left_lst, right_lst)

    def mergerList(self,left_lst: List[int], right_lst: List[int]) -> List[int]:

        left_length = len(left_lst)
        right_length = len(right_lst)
        result = []

        i = 0
        j = 0
        while( i < left_length and j < right_length):
            if(left_lst[i] <= right_lst[j]):
                result.append(left_lst[i])
                i += 1
            else:
                result.append(right_lst[j])
                j += 1
        

        while(i <left_length):
            result.append(left_lst[i])
            i += 1
        
        while(j < right_length):
            result.append(right_lst[j])
            j += 1

        return result
        



