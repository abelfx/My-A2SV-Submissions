# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increase = deque()
        decrease = deque()

        left = 0
        count = 0

        for right in range(len(nums)):
            while increase and increase[-1] > nums[right]:
                increase.pop()
            increase.append(nums[right])

            while decrease and decrease[-1] < nums[right]:
                decrease.pop()
            decrease.append(nums[right])

            while decrease[0] - increase[0] > limit:
                if nums[left] == decrease[0]:
                    decrease.popleft()
                if nums[left] == increase[0]:
                    increase.popleft()
                
                left += 1
            count = max(count, right - left + 1)
        

        return count
