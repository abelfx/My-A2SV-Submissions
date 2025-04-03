# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        n = len(matrix)
        m = len(matrix[0])

        location = 0
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right -= 1
            elif matrix[mid][m-1] < target:
                left += 1 
            elif matrix[mid][0] <= target and matrix[mid][m-1] >= target:
                location = mid
                break
        
        print(location)
        if target not in matrix[location]:
            return False
        return True
        
        
