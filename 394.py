class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0  # 當前重複次數
        curr_str = ''  # 當前字符串
        
        for c in s:
            if c.isdigit():  # 如果是數字
                curr_num = curr_num * 10 + int(c)
            elif c == '[':  # 如果是‘[’
                stack.append((curr_str, curr_num))  # 將當前字符串和重複次數入棧
                curr_str, curr_num = '', 0  # 重置當前字符串和重複次數
            elif c == ']':  # 如果是‘]’
                last_str, num = stack.pop()  # 出棧
                curr_str = last_str + num * curr_str  # 拼接字符串
            else:  # 如果是字母
                curr_str += c  # 將字母添加到當前字符串
        
        return curr_str  # 返回結果字符串