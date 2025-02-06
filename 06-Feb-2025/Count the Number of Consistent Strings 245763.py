# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        
        count = 0
        for i in words:
            bool_check = True
            for j in i:
                if j not in allowed:
                    bool_check = False
            
            if(bool_check == True):
                count +=1
        
        return count
                    

        