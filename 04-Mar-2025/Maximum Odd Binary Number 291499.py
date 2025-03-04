# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count('1')

        if count == 1:
            return ("0" * (len(s) - 1)) + "1"
        else:
            return ("1" * (count - 1)) + ("0" * (len(s) - count)) + "1"