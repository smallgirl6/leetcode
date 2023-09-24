class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([0])
        visited = set([0])
        step = 0
        while queue:
            step += 1
            for i in range(len(queue)):
                number = queue.popleft() # 取出一個數字
                for j in range(1,n+1):
                    next_num = number + j*j # 計算下一個數字
                    if next_num == n: # 找到n，返回步數
                        return step
                    if next_num > n: # 超過n，break
                        break
                    if next_num not in visited:
                        queue.append(next_num)
                        visited.add(next_num)
        return 0