# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""

        for i in word1:
            str1 += i
        for i in word2:
            str2 += i
        
        print(str1)
        print(str2)
        return str1 == str2
        