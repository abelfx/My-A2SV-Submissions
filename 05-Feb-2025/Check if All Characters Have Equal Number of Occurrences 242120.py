# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counted = Counter(s)
        freq = 0
        for keys, values in counted.items():
            freq = values
            break

        for keys, values in counted.items():
            if values != freq:
                return False
        
        return True
            
        