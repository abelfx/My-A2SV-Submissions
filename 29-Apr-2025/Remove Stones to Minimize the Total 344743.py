# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            cur = -heapq.heappop(heap)
            heapq.heappush(heap, -(cur-cur//2))
        return -sum(heap)  
        