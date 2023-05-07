class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recr(node):
            if not node:
                return 0
            # 遞歸處理左子樹和右子樹
            left_depth = recr(node.left)
            right_depth = recr(node.right)
            # 返回當前節點為根的子樹的最大深度(往下遍歷一層深度+1)
            return max(left_depth, right_depth) + 1

        # 從根節點開始遞歸
        return recr(root)