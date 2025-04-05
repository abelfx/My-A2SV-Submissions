# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctd = Counter(nums)
        result = []

        for i in range(k):
            max_value = max(ctd.values())
            for key in ctd.keys():
                if(max_value == ctd[key]):
                    result.append(key)
                    ctd.pop(key)
                    break
        
        return result