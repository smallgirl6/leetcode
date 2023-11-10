#-------------------------------------------BST-------------------------------------------
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            if root.val > val: # 太大往左找比較小的
                root = root.left
            else:
                 root = root.right # 太小往右邊找
        return None