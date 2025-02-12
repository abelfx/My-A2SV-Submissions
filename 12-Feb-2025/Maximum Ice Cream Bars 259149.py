# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()

        counter = 0
        i = 0
        while(coins > 0 and i < len(costs)):
            if coins >= costs[i]:
                coins -= costs[i]
                counter += 1
            
            i += 1
            
        
        return counter
        