class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(root)
        if not root:
            return 0
        queue = [(root,1)] # root 節點位於深度為 1 的位置
        max_depth = 0
        while queue:
            current, depth = queue.pop(0) # (currentNode, depth)
            max_depth = max(max_depth, depth)
            
            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))
        return max_depth