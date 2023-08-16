# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self,root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        
        while queue:

            current_node, depth = queue.pop(0)  

            if not current_node.left and not current_node.right:
                return depth

            if current_node.left:
                queue.append((current_node.left, depth + 1))

            if current_node.right:
                queue.append((current_node.right, depth + 1))
