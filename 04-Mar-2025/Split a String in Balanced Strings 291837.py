# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance_checker = 0
        counter = 0

        for c in s:
            if c == "R":
                balance_checker += 1
            else:
                balance_checker -= 1
            
            if balance_checker == 0:
                counter += 1
        
        return counter