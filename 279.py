class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([(n, 0)])
        visited = set()
        
        while queue:
            remainder, steps = queue.popleft()
            
            if remainder == 0:
                return steps
            for i in range(1, int(math.sqrt(remainder)) + 1):
                next_remainder = remainder - i * i
                
                if next_remainder in visited:
                    continue
                
                visited.add(next_remainder)
                queue.append((next_remainder, steps + 1))