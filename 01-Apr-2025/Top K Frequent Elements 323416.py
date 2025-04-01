# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        result = []

        for i in range(k):
            max_value = max(counted.values())
            for key in counted.keys():
                if(max_value == counted[key]):
                    result.append(key)
                    counted.pop(key)
                    break
        
        return result