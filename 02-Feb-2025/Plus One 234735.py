# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s+= str(i)

        num = int(s)

        num += 1

        result = []

        for i in str(num):
            result.append(int(i))

        
        return result

        