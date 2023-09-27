class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0  # 當前重複次數
        curr_str = ''  # 當前字符串   
        for c in s: 
            if c.isdigit():  # 如果是數字         
                curr_num = curr_num * 10 + int(c) 
            elif c == '[':                        
                stack.append((curr_str, curr_num))  # 將當前字符串和重複次數入stack   
                curr_str, curr_num = '', 0  # 重置當前字符串和重複次數        
            elif c == ']': 
                last_str, num = stack.pop()  # 出stack
                curr_str = last_str + num * curr_str  # 拼接字符串
            else:  # 如果是字母                       
                curr_str += c  # 將字母添加到當前字符串  
        
        return curr_str  # 返回結果字符串

      #1. s = "2[abc]3[cd]ef"   
      #2. c = '2'  >>  if c.isdigit():
      #3. curr_num = 0 * 10 + 2 = 2
      #4. c = '[' >> elif c == '[': 
      #5. stack.append(('', 2))
      #6. 重置 curr_str 和 curr_num 為 '' 和 0
      #7. c = 分別為 'a','b', 'c' >> else:  # 如果是字母
      #8. curr_str = 'abc'
      #9. c = ']' >> c == ']': 
      #10. last_str, num = stack.pop() >>  pop 出 ('', 2) >>NO.5
      #11. curr_str = last_str + num * curr_str  >> last_str(0) + num(2) *curr_str(abc)  = abcabc
      #12. c = '3' >> if c.isdigit(): 
      #13. curr_num = 0 * 10 + 3 = 3
      #14. c = '[' >> elif c == '[':
      #15. stack.append(('curr_str', 3))  >> stack.append(('abcabc', 3)) >>>> NO.11
      #16. 重置 curr_str 和 curr_num 為 '' 和 0
      #17. c = 分別為 'c' ,'d' >> else:  # 如果是字母
      #18. curr_str = 'cd'
      #19. c = ']' >> c == ']': 
      #20. last_str, num = stack.pop() >>  pop 出 ('abcabc', 3) >> NO.15
      #21. curr_str = last_str + num * curr_str  >> last_str(abcabc) + num(3) *curr_str(cd)  = abcabc + cdcdcd
      #22. c = 'ef'  >> else:  # 如果是字母 
      #23  curr_str += c  abcabccdcdcd + ef = abcabccdcdcdef