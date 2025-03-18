# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def preOrder(root, level):
            if not root:
                return
            
            if len(arr) <= level:
                arr.append(float("-inf"))
            
            arr[level] = max(arr[level], root.val)

            preOrder(root.left, level + 1)
            preOrder(root.right, level + 1)
        
        preOrder(root, 0)

        return arr