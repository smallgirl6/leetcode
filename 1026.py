# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, root.val, root.val)])
        max_diff = 0

        while queue:
            node, min_val, max_val = queue.popleft()
            max_diff = max(max_diff, abs(node.val - min_val), abs(node.val - max_val))

            if node.left:
                new_min_val = min(min_val, node.left.val)
                new_max_val = max(max_val, node.left.val)
                queue.append((node.left, new_min_val, new_max_val))

            if node.right:
                new_min_val = min(min_val, node.right.val)
                new_max_val = max(max_val, node.right.val)
                queue.append((node.right, new_min_val, new_max_val))

        return max_diff