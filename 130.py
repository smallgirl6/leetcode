class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        queue = deque()

        # 將邊界上的 'O' 加入隊列
        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    queue.append((i, j))

        # 標記不能被翻轉的 'O'
        while queue:
            x, y = queue.popleft()
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = 'E'
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    queue.append((x+dx, y+dy))

        # 翻轉 'O' 為 'X'，並將 'E' 還原為 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'