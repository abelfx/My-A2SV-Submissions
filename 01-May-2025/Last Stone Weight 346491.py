# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # lets brute force this

        while stones and len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                big = stones.pop()
                small = stones.pop()

                stones.append(big-small)
        
        if stones:
            return stones[0]
        else:
            return 0

            
        