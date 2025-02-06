# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = {}

        min_count = float("inf")
        result = []

        for i, value in enumerate(list1):
            dict[value] = i
        
        for i, value in enumerate(list2):
            if value in dict:
                i_sum = i + dict[value]

                if(i_sum < min_count):
                    min_count = i_sum
                    result = [value]
                elif(i_sum == min_count):
                    result.append(value)
        
        return result


        