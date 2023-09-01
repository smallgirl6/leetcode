class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        column_len, row_len = len(board), len(board[0]) 
        queue = deque()
        
        # 檢查矩陣的所有列（column）的第一個和最後一個元素
        for i in range(column_len): 
            for j in [0, row_len-1 ]: # 只會遍歷兩個值：0 和 row_len-1。會查看第一行和最後一行
                if board[i][j] == "O":
                    queue.append((i, j))
                    
         # 檢查矩陣的第一行和最後一行的所有元素              
        for i in [0, column_len-1 ]: # 只會遍歷兩個值：0 和 column_len-1。會查看第一行和最後一行
            for j in range(row_len):
                if board[i][j] == "O":
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            # 不能超出範圍 且 board[x][y] == 'O'
            if 0 <= x < column_len and 0 <= y < row_len and board[x][y] == 'O':  
                board[x][y] = 'E'
                # 每找到一個 'O'，它周圍可能也是 'O' ，加入到一個待檢查的清單裡
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    queue.append((x+dx, y+dy)) # 原來站在 (x, y)，按照 dx, dy 走過去之後的新座標。


        for i in range(column_len):
            for j in range(row_len):
                if board[i][j] == 'O': # 如果該位置是 'O'，那一定是被 'X' 完全包圍的 'O'，
                                       # 因為所有不應被轉換的 'O' 已經被轉換為 'E' 了
                    board[i][j] = 'X'  # 。所以將它轉換為 'X'。
                elif board[i][j] == 'E': # 將之前標記為 'E' 的位置恢復為 'O'。
                    board[i][j] = 'O'
