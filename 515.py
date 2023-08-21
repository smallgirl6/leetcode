
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        queue = deque([root])

        while queue:
            row_max = float('-inf')
            row_size = len(queue)

            for i in range(row_size):
                node = queue.popleft()
                row_max = max(row_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(row_max)
        return output