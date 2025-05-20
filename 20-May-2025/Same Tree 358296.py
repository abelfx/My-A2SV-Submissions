# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        tree1 = []
        tree2 = []
        def preOrder1(p):
            if not p:
                tree1.append("*")
                return
            
            tree1.append(p.val)
            preOrder1(p.left)        
            preOrder1(p.right)
        
        def preOrder2(q):
            if not q:
                tree2.append("*")
                return
            
            tree2.append(q.val)
            preOrder2(q.left)
            preOrder2(q.right)
            
        
        preOrder1(p)
        preOrder2(q)

        print(tree1)
        print(tree2)

        return tree1 == tree2
        