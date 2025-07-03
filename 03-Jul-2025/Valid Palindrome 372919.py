# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]","", s)

        
        reversed = ""
        for i in range(len(s)-1, -1, -1):
            reversed += s[i]
        
        print(s)
        print(reversed)
        if s == reversed:
            return True
        return False

        