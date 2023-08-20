class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        output = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for i in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            output.append(level_sum / level_count)  

        return output  