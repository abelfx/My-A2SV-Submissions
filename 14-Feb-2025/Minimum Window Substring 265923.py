# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        t_len = len(t)
        t_counter = Counter(t)
        count = 0
        sub_range = [float('-inf'),float('inf')]
        left = 0
        
        for right in range(N):
            if s[right] in t_counter:
                t_counter[s[right]] -= 1
                if t_counter[s[right]] >= 0:
                    count += 1
            while count == t_len:
                if right - left  < sub_range[1] - sub_range[0]:
                    sub_range = [left, right]
                if s[left] in t_counter:
                    t_counter[s[left]] += 1
                    if t_counter[s[left]] > 0:
                        count -= 1
                left += 1

        if sub_range[0] == float('-inf'):
            return ''
        return s[sub_range[0] : sub_range[1] + 1]