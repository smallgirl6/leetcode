# stack         
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = []
        primitive = [] # 暫存當前原始括號字符串

        for c in s:
            if c == "(":
                stack.append(c)
                primitive.append(c)
            else: # c==")"
                stack.pop()
                primitive.append(c)
            
            if not stack:
                result.extend(primitive[1:-1]) # 移除最外層的括號
                primitive = []  #  清空primitive
        
        print(result)
        return "".join(result) 