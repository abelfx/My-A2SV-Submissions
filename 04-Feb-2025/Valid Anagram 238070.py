# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        for i in range(len(s)):
            if(sorted_s[i] != sorted_t[i]):
                return False

        return True
        

    
        