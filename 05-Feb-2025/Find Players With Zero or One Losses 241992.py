# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}

        for winner, loser in matches:
            if winner in winners:
                winners[winner] +=1
            else:
                winners[winner] =1
            if loser in losers:
                losers[loser] +=1
            else:
                losers[loser] =1

        
        print(winners)
        print(losers)


        first_array = []
        second_array = []
        for keys in winners.keys():
          if keys not in losers:
             first_array.append(keys)

        for keys, values in losers.items():
          if values == 1:
            second_array.append(keys)

        
        return [sorted(first_array), sorted(second_array)]




        

        
        