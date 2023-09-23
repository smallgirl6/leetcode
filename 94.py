#Stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 先訪問左子樹，然後訪問根節點，最後訪問右子樹。
# Definition for a binary tree node.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        while stack or root:                                                                                           #stack剩一個2
            # root = [1,null,2,3]
            while root:            # 從根節點1開始           # 根節點2開始       # 根節點3開始
                stack.append(root) # 將1放入stack中          # 將2放入stack中    # 將3放入stack中
                root = root.left   # 1左邊是null跳出while    # 2左邊是3 3設為root # 3左邊是null跳出while
            root = stack.pop()     #　pop出stack中的1     　 # pop出stack中的3　　# pop出stack中的2
            result.append(root.val) #　把1加入result　　　　　　　　　　　　　　　　# 把3加入result　　　# 把2加入result　
            root = root.right      #　確認1的右邊 把1右邊的2設為root　　　　　　　 #　確認3的右邊是null 　#　確認2的右邊是null
        return result