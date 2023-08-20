from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, targetSum - root.val)])
        while queue:
            node, curSum = queue.popleft()
            if not node.left and  not node.right and curSum == 0:
                return True    
            if node.left:
                queue.append((node.left, curSum - node.left.val))
            if node.right:
                queue.append((node.right, curSum - node.right.val))
        return False