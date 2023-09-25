class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_orange = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_orange +=1
                elif grid[row][col] == 2:
                    queue.append((row,col))
        if fresh_orange == 0:
            return 0
        
        minutes = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)] # 右，下，左，上

        while queue:
            size = len(queue)
            for i in range(size):
                queue_row, queue_col = queue.popleft()
                for direction in directions:
                    new_queue_row = queue_row + direction[0]
                    new_queue_col = queue_col + direction[1]
                    if 0 <= new_queue_row < rows and 0 <= new_queue_col < cols and grid[new_queue_row][new_queue_col] == 1:
                        grid[new_queue_row][new_queue_col] = 2
                        fresh_orange -= 1
                        queue.append((new_queue_row,new_queue_col))
            minutes += 1
        
        if fresh_orange == 0:
            return minutes -1
        else:
            return -1