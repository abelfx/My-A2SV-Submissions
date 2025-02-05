# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst = []
        for i in accounts:
            maxim = 0
            for j in i:
                maxim += j
            lst.append(maxim)
            
        
        return max(lst)


          
        
      

        