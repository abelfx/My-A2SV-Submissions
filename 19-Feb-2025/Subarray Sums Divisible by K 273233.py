# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        dict = {0: 1}
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k

            if mod in dict:
                count += dict[mod]
                dict[mod] +=1
            else:
                dict[mod] = 1
            
        return count
