# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dict = Counter(s)
        print(dict)
        result = ""
        while dict['1'] != 1:
            result += "1"
            dict['1'] -= 1
        
        while dict['0'] != 0:
            result += "0"
            dict['0'] -= 1
        
        result += "1"

        return result
        