class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        queue  = deque()
        count = 0
        for char in s:
            if char == "(":
                queue.append(char)
            else: #char == ")"
                if queue:
                    queue.popleft() # 最左邊取出一個"(" 抵銷了一對()
                else:
                    count += 1 #沒有 queue代表沒有"(" ，需要一個"(" 所以count+1
        return count + len(queue) # count =　缺幾個"(" ， len(queue)= queue中剩餘的"("的數量 ， 缺幾個")"