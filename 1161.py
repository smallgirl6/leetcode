#bfs   queue
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = float('-inf')
        max_level = 1
        queue = deque([(root,1)])

        while queue:
            level_size = len(queue)
            level_sum = 0
            level = 0
            for i in range(level_size):
                node, level = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append((node.left, level +1))
                if node.right:
                    queue.append((node.right, level +1))
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
        return max_level