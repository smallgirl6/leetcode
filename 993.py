# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 相同的深度且具有不同的父節點 =  cousins
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        queue = [(root, None, 0)] # node, parent, depath 
        x_info = y_info = None

        while queue:
            next_queue = []
            for node, parent, depath in queue:
                if node.left:
                    next_queue.append((node.left, node, depath +1))
                    
                    if node.left.val == x:
                        x_info = (depath+1, node)
                    if node.left.val == y:
                        y_info = (depath+1, node)

                if node.right:
                    next_queue.append((node.right, node, depath+1))

                    if node.right.val == x:
                        x_info = (depath+1, node)
                    if node.right.val == y:
                        y_info = (depath+1, node)

            if x_info and y_info:
                return x_info[0] == y_info[0] and  x_info[1] != y_info[1] # 相同的深度且具有不同的父節點
            if x_info or y_info:
                return False

            queue = next_queue

        return False
                    
                    