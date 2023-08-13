# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None      
        queue = [root]     
        while queue:
            current = queue.pop(0)  # 取出當前節點
            print(current)
            # 交換當前節點的左右子樹
            current.left, current.right = current.right, current.left         
            # 如果當前節點有左子樹，將其加入隊列
            if current.left:
                queue.append(current.left)
            # 如果當前節點有右子樹，將其加入隊列
            if current.right:
                queue.append(current.right)       
        return root