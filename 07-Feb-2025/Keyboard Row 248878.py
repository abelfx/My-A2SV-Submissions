# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        result = []
        for word in words:
            lower_word = set(word.lower())
            if lower_word <= first_row or lower_word <= second_row or lower_word <= third_row:
                result.append(word)
        

        return result