# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        current_sum = 0
        counter = 0
        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum - goal in count:
                counter += count[current_sum - goal]
            count[current_sum] = count.get(current_sum, 0) + 1
        
        return counter

            