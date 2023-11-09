-------------------------------------------preorder-------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = []
        while stack or root: #當 stack 不為空或者 root 不為空時繼續
            if root: #如果 root 不為空
                if root.val == val: #如果 root 的值剛好等於 val(找到目標!)
                    return root  # 返回 root
                stack.append(root) #將 root 添加到 stack 中
                root = root.left # 把root往左移
            else: #如果 root 為空
                root = stack.pop() # 取出最上面的節點
                root = root.right  # 把root往右移
        return None #找不到目標回傳[]