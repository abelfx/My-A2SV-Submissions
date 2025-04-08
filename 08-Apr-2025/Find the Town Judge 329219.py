# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        h1 = {}
        h2 = {}

        for i in range(1, n+1):
            h1[i] = 0
            h2[i] = 0

        for i, j in trust:
            h1[i] += 1
            h2[j] += 1
        
        judge = -1

        for i in range(1, n+1):
            if h1[i] == 0 and h2[i] == n-1:
                judge = i
        
        return judge
                
