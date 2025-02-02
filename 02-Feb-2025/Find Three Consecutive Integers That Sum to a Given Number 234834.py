# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = num//3

        lst = [middle-1, middle, middle+1]

        result = 0
        for i in lst:
            result = result + i

        if result == num:
            return lst
        else:
            return []
        