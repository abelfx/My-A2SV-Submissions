# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles

        while(numBottles >= numExchange):
            result += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
           

        
        return result