# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = int(a, 2)
        b = int(b, 2)
        r = n + b
        return bin(r)[2:]
        