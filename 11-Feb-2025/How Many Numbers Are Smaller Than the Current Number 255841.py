# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter_dict = defaultdict(int)

        result = []
        for i in nums:
            counter_dict[i] += 1
        
        for i in nums:
            num = 0
            for keys, values in counter_dict.items():
                if keys < i:
                    num += values
            result.append(num)
        
        return result

        