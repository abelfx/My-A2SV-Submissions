# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        if sorted(arr) == arr:
            return []

        res = []

        for x in range(len(arr), 0, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res

        