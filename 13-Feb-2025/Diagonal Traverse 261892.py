# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        N = len(matrix) 
        M = len(matrix[0])
        
        result = [] 
        intermediate = []
        
        for d in range(N + M - 1):
            intermediate.clear()
            
            if d < M:
                r = 0
                c = d
            else:
                r = d - M + 1
                c = M - 1

            
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result        