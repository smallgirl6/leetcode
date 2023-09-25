# #bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # 如果 grid 不存在，則返回 0
            return 0

        height,width = len(grid),len(grid[0]) # 獲取 grid 的行和列
        landscount =0  # 計數島嶼的數量
        visited = set()  # 已訪問的島嶼
    
        for i in range(height): # 遍歷 grid 中的每一列
            for j in range(width): # 遍歷 grid 中的每一行
                if grid[i][j] == '1' and (i, j) not in visited: # 如果當前位置是島嶼（值為 '1'）且未被訪問過
                    landscount += 1 # 增加島嶼計數器
                    queue = collections.deque() # 創建一個 queue
                    queue.append([i, j])   # 加入初始值 起始點為目前位置

                    while queue: 
                        x, y = queue.popleft() # 從 deque 中取出一個位置, x 和 y 分別代表 grid中的行和列

                        if (x,y) in visited: # 如果位置已經訪問過，則跳過這個位置
                            continue
                        visited.add((x,y)) # 將當前位置標記為已訪問
                        
                        # 如果位置是島嶼且未被訪問過 將目前位置的上、下、左、右四個方向的加入 queue 中
                        #  x 對應到 height（高度，行數），y 對應到 width（寬度，列數）。
                        # 上方是否為 '1'，若是，則表示可以將島嶼向上擴展，因此可以將(x-1, y)加入queue中進行處理
                        if x > 0 and grid[x-1][y] == '1':
                            queue.append((x-1, y))
                        # 下方是否為 '1'，若是，則可以將島嶼向下擴展，因此可以將(x+1, y)加入queue中進行處理。
                        if x < height-1 and grid[x+1][y] == '1':
                            queue.append((x+1, y))
                        if y > 0 and grid[x][y-1] == '1':
                            queue.append((x, y-1))
                        if y < width-1 and grid[x][y+1] == '1':
                            queue.append((x, y+1))
        return landscount # 返回島嶼計數器的值