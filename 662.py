# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            level_length = len(queue)
            first_node, first_index = queue[0] # 當層階級第一個索引
            last_node, last_index = queue[-1] # 當層階級最後一個索引

            max_width = max(max_width, last_index - first_index + 1)


            for _ in range(level_length):
                curr_node, curr_index = queue.popleft()
                # 如果一個節點在第i個位置，那麼它的左子節點會在2 * i的位置，它的右子節點會在2 * i + 1的位置
                if curr_node.left:
                    queue.append((curr_node.left, 2 * curr_index))
                if curr_node.right:
                    queue.append((curr_node.right, 2 * curr_index + 1))
                    
        return max_width