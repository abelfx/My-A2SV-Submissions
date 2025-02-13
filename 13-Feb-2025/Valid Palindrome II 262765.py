# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1

        while(i<j):
            if (s[i] == s[j]):
                i+=1
                j-=1
            else:
                return self.palindrome(s, i+1, j) or self.palindrome(s, i, j-1)
            
        return True
        

    def palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left+=1
                right-=1
        
        return True
                        
        
        