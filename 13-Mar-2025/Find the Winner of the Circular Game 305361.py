# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = []
      
        for i in range(1, n+1):
            lst.append(i)
        
        pointer = 0
        while len(lst) > 1:
            pointer = ((pointer + (k-1)) % len(lst))
            lst.pop(pointer)
        
        return lst[0]
            



        
        

       