# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0] * len(nums)
        for i, j in requests:
            count[i] += 1
            if j + 1 < len(count):
                count[j+1] -= 1

        cur = 0
        for i in range(len(count)):
            count[i] += cur
            cur = count[i]
        
        nums = sorted(nums, reverse=True)
        count = sorted(count, reverse=True)

        summ = 0
        for n, c in zip(nums, count):
            summ += n * c
        
        mod = pow(10, 9) + 7
        return summ % mod