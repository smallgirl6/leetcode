# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_tilt = 0
        stack = [(root, 0, 0)]

        post_order_stack = []
        
        while stack:
            node, _, _ = stack.pop()
            post_order_stack.append(node)
            
            if node.left:
                stack.append((node.left, 0, 0))
            if node.right:
                stack.append((node.right, 0, 0))
        
        while post_order_stack:
            node = post_order_stack.pop()
            
            left_sum = node.left.val if node.left else 0
            right_sum = node.right.val if node.right else 0
            
            node.val += left_sum + right_sum
            total_tilt += abs(left_sum - right_sum)
            
        return total_tilt