# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:

        def split(path, i):
            if i == len(s):
                for j in range(1, len(path)):
                    if path[j]+1 != path[j-1]:
                        return False  

                return len(path) >= 2

            num = 0
            for j in range(i, len(s)):
                num = (num * 10) + int(s[j])
                if not path or path[-1] - 1 == num:
                    path.append(num)
                    if split(path, j+1):
                        return True
                    path.pop()
            
            return False
        

        return split([], 0)