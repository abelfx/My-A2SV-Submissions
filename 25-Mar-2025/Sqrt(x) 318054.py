# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt_root = 0
        l = 0
        r = x

        while l<=r:
            mid = (l+r)//2

            if mid * mid <= x:
                sqrt_root = mid
                l = mid + 1
            else:
                r = mid -1
        
        return sqrt_root
        