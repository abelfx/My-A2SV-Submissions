# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        self.n = len(nums)
        self.q = len(queries)
        left = 0
        right = self.q + 1


        def works(mid):
            diff = [0] * (self.n + 1)

            for s, e, v in queries[:mid]:
                diff[s] += v
                diff[e+1] -= v

            for i in range(1, len(diff)):
                diff[i] += diff[i-1]
            
            for i in range(self.n):
                if nums[i] > diff[i]:
                    return False
            
            return True
                


        while left < right:
            mid = (left + right) // 2

            if works(mid):
                right = mid
            else:
                left = mid + 1
        
        if left == self.q + 1:
            return -1

        return left



        