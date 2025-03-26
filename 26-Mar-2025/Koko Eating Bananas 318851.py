# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 1

        def goodd(mid, h):
            count = 0
            for i in piles:
                count += ceil(i / mid)
            if count <= h:
                return True
            return False



        while left <= right:
            mid = (left + right) // 2

            if goodd(mid, h):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        
        return ans

       