# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.lst = []
        def traversal(root):
            if not root:
                return
            
            self.lst.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return len(Counter(self.lst)) == 1
            
