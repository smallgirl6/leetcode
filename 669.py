# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 如果節點值小於low，修剪左子樹，返回右子樹的修剪結果
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # 如果節點值大於high，修剪右子樹，返回左子樹的修剪結果
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # 節點值在範圍內，遞歸處理左右子樹
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root