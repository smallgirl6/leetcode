class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = [(root, 1)]
        max_depth = 0
        
        while queue:
            current, depth = queue.pop(0)  
            max_depth = max(max_depth, depth)
            
            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))

        return max_depth
