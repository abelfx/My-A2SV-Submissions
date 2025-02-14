# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        maxx = 0
        while i < j:
            if height[i] < height[j]:
                maxx = max(maxx, height[i] * (j - i))
                i += 1
            else:
                maxx = max(maxx, height[j] * (j - i))
                j -= 1
        
        return maxx


