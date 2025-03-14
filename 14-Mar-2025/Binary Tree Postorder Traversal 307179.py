# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.lst = []
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                self.lst.append(root.val)
        
        postorder(root)

        return self.lst


        