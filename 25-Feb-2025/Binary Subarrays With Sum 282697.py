# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        curr_sum = 0
        counter = 0
        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum - goal in count:
                counter += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1
        
        return counter

            