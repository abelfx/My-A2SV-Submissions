# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covering_set = set()

        for start, end in ranges:
            for i in range(start, end + 1):
                covering_set.add(i)

        print(covering_set)
        for i in range(left, right + 1):
            if i not in covering_set:
                return False
                
        return True
