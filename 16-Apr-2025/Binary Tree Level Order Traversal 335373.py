# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        current_level = 0
        current_level_array = []
        total_levels = []
        queue = deque([(root, 0)])

        while queue:
            node, node_level = queue.popleft()

            if not node:
                continue
            
            if node_level != current_level:
                total_levels.append(current_level_array)
                current_level_array = []
                current_level += 1
            
            current_level_array.append(node.val)
            queue.append((node.left,  current_level + 1))
            queue.append((node.right, current_level + 1))
        
        if current_level_array:
            total_levels.append(current_level_array)
        
        return total_levels