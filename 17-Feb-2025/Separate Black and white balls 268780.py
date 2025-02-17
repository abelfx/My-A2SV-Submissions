# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        counter = 0
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                counter+=1
            else:
                result += counter
        
        return result