# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def recr(node, _list): # 遍歷樹節點，並把節點的值加入到_list列表中
            if node is None:        # 如果節點為空
                _list.append(None)  # 在 _list 中加入一個 None
                return
            _list.append(node.val)  # 否則，在 _list 中加入節點的值
            recr(node.left , _list) # 然後遞歸調用 recr 函數遍歷左右子樹
            recr(node.right, _list)
        p_list =[]                  # 初始化兩個列表 p_list 和 q_list。
        q_list= []
        recr(p, p_list)              # 遍歷 p 樹，把節點的值加入到 p_list 中
        recr(q, q_list)
        return p_list == q_list      # 判斷 p_list 和 q_list 是否相等




