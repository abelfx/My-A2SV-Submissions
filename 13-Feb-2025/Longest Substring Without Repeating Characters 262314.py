# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0

        dict = {}
        # max_len = 3
        # dict = {"a" : 3, "b": 4, "c": 5}
        # i = 3

        for j, char in enumerate(s):
            if char in dict and dict[char] >= i:
                i = dict[char] + 1
            
            max_len = max(max_len, j - i + 1)
            dict[char] = j

        return max_len
        
        