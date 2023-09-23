#queue
#找最後一層的最左邊葉子節點
#把所有節點依序從最上層最右邊放進去queue
#1→3→2→6→5→4→7　最後一個就是答案了
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            
        return node.val 
        