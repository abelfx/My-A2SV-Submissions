# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        result = []
        for word in words:
            checker = True
            for char in word:
               if word.count(char) > chars.count(char):
                checker = False
                break

            if checker:
                result.append(word)
        
        total = 0
        for word in result:
            total += len(word)

        return total