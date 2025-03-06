# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_s = []
        res_t = []
        for char in s:
            if char == "#":
                if len(res_s) != 0:
                    res_s.pop()
            else:
                res_s.append(char)

        for char in t:
            if char == "#":
                if len(res_t) != 0:
                    res_t.pop()
            else:
                res_t.append(char)
        
        if res_s == res_t:
            return True
        return False
        
        