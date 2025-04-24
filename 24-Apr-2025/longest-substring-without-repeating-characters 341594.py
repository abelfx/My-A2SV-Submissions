# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        i = 0
        j = 1
        counter = 0
        while j < len(s):
            ss = s[i:j+1]
            dictt = set(ss)
            if len(ss) == len(dictt):
                counter = max(len(ss), counter)
                j+=1
            if len(ss) != len(dictt):
                i+=1 
            
        return counter
        