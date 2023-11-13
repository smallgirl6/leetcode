#dfs的空間複雜度和時間複雜度都是O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: # 樹是空的
            return True # 這棵樹被視為是平衡的
    
        stack = [] # stack的每個元素是一個元組 (node, visited)，node 是樹中的節點，visited 是表示這個節點是否已經被“處理過”
        node_info = {}  # 每個節點的左右子樹高度資訊 #node_info = {15:0,7:0}

        # 先處理root
        stack.append((root, False))
        # 當一個節點第一次被放入stack中時，visited 設定為 False，表示這個節點還沒有被處理。
        # 節點和其子節點被遍歷後，節點會再次被放入stack中，但這次 visited 設定為 True，表示其子節點已被訪問過，現在需要計算這個節點的高度並檢查其平衡性。

        while stack:
            node, visited = stack.pop() # (3, False) →　(20, False)　(9, False)　→　(7, False)(15, False)
            if node:
                if visited: # 節點的子節點已經遍歷過，現在可以計算該節點的高度　(7, True)　(15, True)
                    # 取得目前節點左右子節點的高度。 如果子節點不存在（None），會傳回預設值 0。　(7→0)　(15→0)
                    left_height = node_info.get(node.left, 0)
                    right_height = node_info.get(node.right, 0)
                    # 檢查目前節點的左右子樹的高度差是否超過1。如果高度差超過1，則樹不平衡，回傳 False。
                    if abs(left_height - right_height) > 1:
                        return False
                    # 記錄當前節點的高度
                    node_info[node] = 1 + max(left_height, right_height) # 當前節點等於左右子樹的最大高度加1（加1是因為要加上目前節點本身）

                else: #如果節點未造訪過，將其重新入stack，並將左右子節點入stack
                    stack.append((node, True)) # (3, True)　→　(20, True)　(9, True)　→　(7, True)　(15, True)
                    stack.append((node.right, False)) # (20, False)　→　　(7, False)
                    stack.append((node.left, False)) #(9, False)　　 →　　(15, False)
        # 檢查整個樹的根節點的平衡性。
        # 之前的程式碼已經確保了所有子樹也都是平衡的，所以可以確認整棵樹是平衡的。
        # 如果這個條件滿足，傳回 True；否則，高度差超過1，傳回 False。
        return abs(node_info.get(root.left, 0) - node_info.get(root.right, 0)) <= 1

        