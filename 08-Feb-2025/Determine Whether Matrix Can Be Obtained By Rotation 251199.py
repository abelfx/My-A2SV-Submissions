# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        
        for i in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat)]
            mat.reverse()
        
        return False

        


            
        