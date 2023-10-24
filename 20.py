class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # 創建一個 stack 列表
        mapping = {')': '(', '}': '{', ']': '['}  # 創建一個  mapping 字典存關和開的括號之間的映射關係
        for char in s:
            if char in mapping:  # 處理字符為關閉括號的情況　')'　'}'　']'
                if not stack or stack[-1] != mapping[char]: 
                # 1. 如果 stack 為空，則代表關閉括號沒有對應的開放括號
                # 2. 檢查 stack 的最上面(最後)的元素stack[-1] 是否與目前關閉括號所對應的開放括號 mapping[char]匹配
                    return False
                stack.pop() # 遇到關閉括號時，從 Stack 中取出對應的開放括號(從 Stack 中取出最上面的元素)
            else:                #  如果 char 是開放括號，則將其加入 stack 
                stack.append(char)  
        return not stack    # 當 Stack 中沒有元素時為 True，否則為 False