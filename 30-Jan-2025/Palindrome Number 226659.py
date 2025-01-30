# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        orgx = x
        reverse = 0

        while (orgx > 0):
            reverse = reverse*10 + orgx%10
            orgx = orgx//10
            
        if(x == reverse):
            return True
        
        return False

        