# queue    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # BFS先嘗試所有只有一個括號的組合，然後是兩個括號的組合，直到有 2n 個括號的組合
        result = []
        queue = deque([(0, 0, "")])
        while queue: 
            left, right, cur_string = queue.popleft()
            if len(cur_string) == 2*n:
                result.append(cur_string)
            if left < n:
                queue.append((left+1, right, cur_string + "("))
            if right < left:
                queue.append((left, right+1, cur_string + ")"))
        return result
