# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        ans = 1
        direction = 1

        
        for i in range(time):
            if(ans == n):
                direction = -1
            if(ans == 1):
                direction = 1
            ans = ans + (1 * direction)
          

        
        return ans
            


          

        