# ------------------------------------------- bfs ------------------------------------------- 
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        queue = collections.deque()
        queue.append(root)

        while queue:# 遍歷queue
            node = queue.popleft() # 將queue中的node一一取出
            # 如果當前node為 None，則跳過當前循環，繼續尋找下一個node
            if node is None:
                continue               
            # 如果目前node的值等於目標值 val，則返回目前node
            if node.val == val:
                return node
            # 如果目前node的值大於目標值 val，則將目前node的左子節點加入隊列中繼續搜索。
            # 目前node的值大於目標值 val 時，如果往右子樹搜索，那麼右子樹中所有節點的值都會比目前node的值大於或等於 val，
            # 左子樹中所有node的值都比目前node的值小於 val，
            # 因此只有繼續在左子樹中搜索才有可能找到值為 val 的節點，所以要將目前node的左子節點加入隊列中繼續搜索
            if node.val > val:    
                queue.append(node.left)
            else:    
                queue.append(node.right)
        # 如果遍歷完整棵樹仍然沒有找到目標，則返回 None。
        return None