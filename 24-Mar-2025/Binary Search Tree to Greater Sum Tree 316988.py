# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.result = []
        def dfs(root):
            if not root:
                return
            self.result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        sorted_result = sorted(self.result)
        dict = defaultdict(int)
        for i in range(len(sorted_result)):
            dict[sorted_result[i]] = sum(sorted_result[i:])
        
        def bst_gst(root):
            if not root:
                return

            root.val = dict[root.val]
            bst_gst(root.left)
            bst_gst(root.right)
        
        bst_gst(root)

        return root

        