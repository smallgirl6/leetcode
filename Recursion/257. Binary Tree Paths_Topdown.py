# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths =[]
        def recr(node, path):
            if not node: #首先判斷節點是否為空
                return 
            path += f"{node.val}"
            if not node.left and not node.right: 
                paths.append(path)
                return

            recr(node.left, path + "->")
            recr(node.right, path + "->")
             
        recr(root,"")    
        return paths