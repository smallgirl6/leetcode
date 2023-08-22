class Solution:
     def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        output = 0
        queue = deque([(root,0)])
        while queue:
            node, prevDepath  = queue.popleft()
            curDepath = prevDepath +1 
            output = max(output,curDepath)
            if node.left:
                queue.append((node.left, curDepath))
            if node.right:
                queue.append((node.right, curDepath))
        return output
