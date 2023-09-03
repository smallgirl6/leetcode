class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        # Define directions for moving up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    queue = deque([(i, j)])

                    # BFS to explore the island and mark it as visited
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1":
                                grid[new_x][new_y] = "0"  # Mark as visited
                                queue.append((new_x, new_y))

                    # Mark the starting point as visited
                    grid[i][j] = "0"

        return count