# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def sum_root(root, path):
            if not root:
                return
            path = 10 * path + root.val
            if not root.left and not root.right:
                 self.total += path
            else:
                sum_root(root.left, path)
                sum_root(root.right, path)
        
        sum_root(root, 0)

        return self.total
            

            

