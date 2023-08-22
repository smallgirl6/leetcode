#bfs   queue
class Solution:
     def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: # 如果二叉樹的根節點為空，即樹的深度為 0
            return 0
        ans = 0 # maximun depath

        queue= collections.deque() # 儲待處理的node
        queue.append((root,0)) # 將root和深度 0 添加到queue的尾部，表示從root開始的深度為 0

        while queue: # 當queue不為空時，繼續遍歷二叉樹
            node, prevDepth =queue.popleft() # 從queue的頭部取出一個節點和其深度

            curDepth = prevDepth +1 # 計算目前node的深度，即其父節點深度加 1(加一層)
            ans = max(ans, curDepth)# 如果目前node的深度大於最大深度，則將最大深度更新為目前node的深度

            if node.left: # 如果目前node有左子樹，則將左子樹和新的深度加入queue中
                queue.append((node.left, curDepth))
            if node.right:# 如果目前node有右子樹，則將右子樹和新的深度加入queue中
                queue.append((node.right, curDepth))
        return ans  # 傳回最大深度