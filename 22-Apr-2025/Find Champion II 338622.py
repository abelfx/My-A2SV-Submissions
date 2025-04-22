# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0 and n == 1:
            return 0
        checker = set()
        teams = [i for i in range(n)]
        winner = set()
        loser = set()
        for edge in edges:
            winner.add(edge[0])
            loser.add(edge[1])
            checker.add(edge[0])
            checker.add(edge[1])
        
        if len(checker) != n:
            return -1

        
        winners = []
        for i in teams:
            if i in winner and i not in loser:
                winners.append(i)
        
        if len(winners) == 1:
            return winners[0]

        return -1
                



        