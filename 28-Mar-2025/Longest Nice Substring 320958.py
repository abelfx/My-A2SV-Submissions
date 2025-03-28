# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
 
        def longest_subring(s):
            if len(s) <= 1:
                return ""

            set_s = set(s)
            for i, char in enumerate(s):
                opposite_case = char.swapcase()
                if opposite_case not in set_s:
                    left = longest_subring(s[:i])
                    right = longest_subring(s[i+1:])
                    if len(left) >= len(right):
                        return left
                    return right
                
            return s
        
        return longest_subring(s)

















        # for i in range(len(s)):
        #     for j in range(1, len(s)):
               

                

        