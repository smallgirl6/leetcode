# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans_node = None     # 初始化搜尋結果的節點為空

        def recr(node):     # 定義recr函式
            # 用搜尋結果節點，因為需要在函式外部使用，所以使用 nonlocal 關鍵字
            nonlocal ans_node

            if node is None:# 如果目前的節點為空，表示搜尋失敗，回傳 False
                return False

            if node.val == val: # 如果目前節點的值等於搜尋值，表示找到目標節點         
                ans_node = node # 設定搜尋結果為目前節點
                return True     # 回傳 True 表示已找到目標節點
            
            elif node.val < val:  # 如果目前節點的值比搜尋值小，往右子樹搜尋
                if recr(node.right): #  如果右子樹中有找到目標節點
                    return True      # 回傳 True 表示已找到目標節點

            else:                  # 如果目前節點的值比搜尋值大，往左子樹搜尋
                if recr(node.left):# 如果左子樹中有找到目標節點
                    return True    # 回傳 True 表示已找到目標節點

            return False           # 如果沒有找到目標節點，回傳 False

        recr(root)                # 開始遞迴搜尋二叉搜索樹，從root節點開始
        return ans_node           # 回傳搜尋結果節點




