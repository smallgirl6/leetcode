# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: # 左右兩邊都沒有東西
            return True
        queue = [root,root] # 將根節點兩次加入queue中，為了之後可以同時比較它的左、右子節點
        print(queue)
        while queue:
            node1 = queue.pop(0) #left   
            node2 = queue.pop(0) #right  
            if not node1 and not node2: # node1和node2若都不為None，代表下面還有東西，所以繼續
                continue
            if not node1 or not node2 or node1.val != node2.val: # 若node1和node2其中一個是None代表不相等
                                                                 # 或是裡面的val不相等
                return False

            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True