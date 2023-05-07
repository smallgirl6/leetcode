# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def recr(node):
            if not node: #首先判斷節點是否為空
                return []
            if node.left is None and node.right is None: #如果節點是葉節點，則返回一個包含該節點值的列表。
                return [str(node.val)]
                
            left_list =recr(node.left)
            right_list =recr(node.right)
             
             #vist
            result=[]
            # 遍歷左子樹和右子樹中的所有節點值
            for val in left_list + right_list:
                #node的值和子節點的值連接起來，形成一個路徑字串，加入結果列表result中
                result.append(str(node.val)+ "->" + val)
            return result

        return recr(root)