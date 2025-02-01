# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        combo = ""

        for i in s:
            combo = combo + str((ord(i) - 96))

        for sth in range(k):
            sums = 0
            for i in combo:
                sums += int(i)
            combo = str(sums) 

        
        return sums
        


        