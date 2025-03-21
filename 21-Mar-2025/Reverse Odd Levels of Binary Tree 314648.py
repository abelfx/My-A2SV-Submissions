# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        q = deque([root])
        i = 0

        while q:

            if i % 2 != 0:
                left = 0
                right = len(q) - 1

                while left < right:
                    q[left].val, q[right].val = q[right].val, q[left].val
                    left += 1
                    right -=1


            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i += 1
        
        return root
        
        


            
