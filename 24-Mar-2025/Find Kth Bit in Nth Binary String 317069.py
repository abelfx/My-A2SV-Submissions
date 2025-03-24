# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def __init__(self):
        self.counter = 0
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n):
            sth = self.revert(s)
            s += "1"
            s += sth
        return s[k-1]
        
    def revert(self, s):
        result = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                result += "1"
            else:
                result += "0"
        return result
