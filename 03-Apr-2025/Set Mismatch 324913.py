# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dictt = Counter(nums)
        s = set(nums)
        res = []
        for keys, values in dictt.items():
            if values == 2:
                res.append(keys)
        
        for i in range(1, len(nums)+1):
            if i not in s:
                res.append(i)
        
        return res