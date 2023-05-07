class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 如果當前節點為空，返回False
        if root is None:
            return False
        
        # 如果當前節點為葉子節點，檢查當前節點的值是否等於目標和
        if root.left is None and root.right is None:
            return root.val == targetSum
        
        # 如果當前節點不是葉子節點，將問題轉化為是否存在一條從根節點到某個葉子節點的路徑
        # 路徑和為 targetSum - root.val (目標總和減去當前節點的值為新的目標總和)
        # 遞歸處理左子樹和右子樹 呼叫 self.hasPathSum() 函數，以當前節點的左子樹和右子樹為根節點
        left_res = self.hasPathSum(root.left, targetSum - root.val)
        right_res = self.hasPathSum(root.right, targetSum - root.val)
        
        # 如果左子樹或右子樹存在符合要求的路徑，返回True
        if left_res or right_res:
            return True
        
        # 如果左子樹和右子樹都不存在符合要求的路徑，返回False
        return False