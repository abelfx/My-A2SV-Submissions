# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
       
        def max_diff(root, m):
            if not root:
                return float("inf"), float("-inf")

            left = max_diff(root.left, m)
            right = max_diff(root.right, m)

            min_val = min(root.val, min(left[0], right[0]))
            max_val = max(root.val, max(left[1], right[1]))

            m[0] = max(m[0], max(abs(min_val - root.val), abs(max_val - root.val)))    

            return min_val, max_val
        
        m = [0]
        max_diff(root, m)
        return m[0]

       

        
            
            
        