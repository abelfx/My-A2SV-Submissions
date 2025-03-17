# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.result = TreeNode(0)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search_node(root, val):
            if root == None:
                return None
            if val > root.val:
                search_node(root.right, val)
            elif val < root.val:
                search_node(root.left, val)
            else:
                self.result.left = root
                return
        
        search_node(root, val)
        return self.result.left
        