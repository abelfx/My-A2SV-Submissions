# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_int = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C":100, 'D':500, "M":1000
        }

        num = 0
        for i in range(len(s)):
            if( i < len(s) - 1 and rom_int[s[i]] < rom_int[s[i+1]]):
                num = num - rom_int[s[i]]
            else:
                num = num + rom_int[s[i]]

        
        return num
            

        