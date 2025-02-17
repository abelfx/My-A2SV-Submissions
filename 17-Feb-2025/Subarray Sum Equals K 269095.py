# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        counter = 0
        prefix_sum = 0
        dict = defaultdict(int)

        dict[0] = 1

        for num in nums:
            prefix_sum += num
            if prefix_sum-k in dict:
                counter += dict[prefix_sum - k]
            dict[prefix_sum] = dict[prefix_sum] + 1
                
        return counter