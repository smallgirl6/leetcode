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
        stack = [(root,False)] #未訪問False #訪問過True
        sum_stack = []
        total_tilt = 0

        while stack:
            node, visted = stack.pop()
            if visted:
                left_sum = sum_stack.pop() if node.left else 0
                right_sum = sum_stack.pop() if node.right else 0
                total_tilt += abs(left_sum - right_sum)
                sum_stack.append(node.val + left_sum + right_sum)
            else: # not visted
                stack.append((node,True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))    
        return total_tilt
 