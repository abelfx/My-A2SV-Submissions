# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # let us optimize this using heap
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            big = heapq.heappop(max_heap)
            small = heapq.heappop(max_heap)
            if abs(big) != abs(small):
               heapq.heappush(max_heap, -(abs(big) - abs(small)))

        if len(max_heap) == 1:
            return abs(max_heap[0])
        else:
            return 0

            
        