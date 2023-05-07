# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def recr(node):
            # 如果根節點為空，返回None
            if node is None:
                return None
            # 如果根節點的值等於val，返回根節點
            if node.val == val:
                return node
            # 如果根節點的值大於val，遞歸左子樹
            elif node.val > val:
                return recr(node.left)
            # 如果根節點的值小於val，遞歸右子樹
            else:
                return recr(node.right)
            
        return recr(root)




