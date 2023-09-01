class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)  # 將 deadends 轉換成一個集合，方便查詢
        if '0000' in dead_set or target in dead_set:  # 如果起點或終點是死亡號碼，直接返回 -1
            return -1
        
        queue = deque([('0000', 0)])  # 初始化一個隊列，裡面放入起點和當前的步數
        visited = set(['0000'])  # 初始化一個已經訪問過的集合，避免重複訪問
        
        while queue:
            node, depth = queue.popleft()  # 從隊列中取出一個節點和它的深度（也就是步數）
            if node == target:  # 如果這個節點就是目標，返回深度（也就是最少的轉動次數）
                return depth
            
            for i in range(4):  # 對於這個節點的每一個輪子
                for d in [-1, 1]:  # 每一個輪子都有兩種轉動方式：向前（+1）和向後（-1）
                    next_node = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]  # 計算轉動後的狀態
                    if next_node not in visited and next_node not in dead_set:  # 如果這個狀態還沒有訪問過，也不是死亡號碼
                        visited.add(next_node)  # 把它加入到已經訪問過的集合裡
                        queue.append((next_node, depth + 1))  # 把它加入到隊列裡，深度（步數）加 1
        
        return -1  # 如果隊列空了還沒有找到目標，返回 -1