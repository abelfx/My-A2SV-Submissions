# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert_value(root, val):
            if val > root.val and root.right == None:
                root.right = TreeNode(val)
                return
            elif val < root.val and root.left == None:
                root.left = TreeNode(val)
                return

            if val > root.val:
                insert_value(root.right, val)
            elif val < root.val:
                insert_value(root.left, val)

        if root:
            insert_value(root, val)
            return root
        else:
            return TreeNode(val)
        

        