# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image[0])
        n=len(image)
        v=[[0]*m for i in range(n)]

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]  

        q = deque([(sr,sc)])
        v[sr][sc] = 1
        s=image[sr][sc]
        while(q):
            r,c = q.popleft()
            image[r][c]=color
            for z in range(4):
                nrow, ncol = r + delRow[z], c + delCol[z]
                if (0 <= nrow < n and 0 <= ncol < m) and (not v[nrow][ncol]) and (image[nrow][ncol] == s):
                        v[nrow][ncol] = 1
                        q.append((nrow, ncol))
        return image
                        
