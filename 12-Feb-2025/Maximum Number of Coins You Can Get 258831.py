# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        summ = 0
        i = len(piles) - 2

        for _ in range(len(piles)//3):
            summ += piles[i]
            i -= 2

        return summ