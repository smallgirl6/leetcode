from typing import Optional  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 初始化flag
        found_ans_flag = False

        # 定義 recr，處理每個節點，並遞歸處理左右子樹
        def recr(node, curSum):
            # 引用上層函數中的標誌位
            nonlocal found_ans_flag

            # 如果已經找到路徑，退出遞歸
            if found_ans_flag:
                return

            # 處理空節點
            if node is None:
                return

            # 處理當前節點
            # 計算路徑和
            curSum += node.val

            # 如果當前節點是葉子節點且路徑和等於目標的路經和
            if node.left is None and node.right is None and curSum == targetSum:
                # 就代表符合要求的路徑，更新flag為TRUE
                found_ans_flag = True
                return

            # 遞歸處理左右子樹
            recr(node.left, curSum)
            recr(node.right, curSum)

        # 從根節點開始遞歸處理
        recr(root, 0)

        # 返回flag
        return found_ans_flag

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

hasPathSum_instance = Solution()
hasPathSum_result = hasPathSum_instance.hasPathSum(root=node1, targetSum=5)

print(hasPathSum_result)
