# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        end = len(s) - 1
        start = end

        while start >= 0 and s[start] != " ":
            start -=1
        

        return end - start