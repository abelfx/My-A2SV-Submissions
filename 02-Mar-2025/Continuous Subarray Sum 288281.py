# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_seen = {0:-1}
        prefix_mod = 0
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] >= 2:
                    return True
            else:
                mod_seen[prefix_mod] = i
        
        return False
