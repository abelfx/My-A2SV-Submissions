# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        tot_even = sum(x for x in nums if x % 2 == 0)

        result = []
        for val, indx in queries:
            if nums[indx] % 2 == 0: 
                tot_even -= nums[indx]

            nums[indx] += val

            if nums[indx] % 2 == 0:
                tot_even += nums[indx]
            
            result.append(tot_even)

        return result
            





            



        