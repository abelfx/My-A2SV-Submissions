# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recurse(root):
            if not root:
                return 0
            left = 1 + recurse(root.left)
            right = 1 + recurse(root.right)

            return max(left, right)
           
        
        return recurse(root)
    