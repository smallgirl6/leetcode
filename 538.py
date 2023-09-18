# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        total_sum = 0
        cur_node = root
        while stack or cur_node:
            while cur_node:  # cur_node 不是空的
                stack.append(cur_node)
                cur_node = cur_node.right

            cur_node = stack.pop() # 從stack取出最後一個節點（下一個需要處理的最大節點）
            total_sum += cur_node.val
            cur_node.val = total_sum

            cur_node = cur_node.left
        
        return  root