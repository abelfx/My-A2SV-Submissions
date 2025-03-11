# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
        
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
            
        if n == 1:
            return True
        
        return n % 4 == 0 and self.isPowerOfFour(n // 4)
        


    

        