# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
        # to heapify -- O(k)
        # we iterate through n-k elements -- n-k(logk)
        # time compelexity = O(n + n-k(logk))-- O(k logk) -- O(logk)
        