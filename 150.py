# 逆波蘭表示法（Reverse Polish Notation，RPN）的工作方式是按照從左到右的順序解析 tokens，並使用stack來暫存運算元，直到遇到運算子為止。
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # 存儲數字  和 運算結果

        # ["2","1","+","3","*"]
        # 遇到 "2" else:stack.append(int(token)) ：append到stack => stack = [2]
        # 遇到 "1" else:stack.append(int(token)) ：append到stack => stack = [2, 1]
        # 遇到 "+" if token in "+-*/": pop 2和1，相加得到3， stack.append(a+b) 將3 append到stack => stack = [3]
        # 遇到 "3" else:stack.append(int(token)) ：append到stack => stack = [3, 3]
        # 遇到 "*" if token in "+-*/": pop 3和3：彈出3和3，相乘得到9，將9 append到stack => stack = [9]
        for token in tokens:
            if token in "+-*/":
                # 先彈出的數值作為第二個運算元（b），然後再彈出的數值作為第一個運算元（a）
                b = stack.pop() # 從堆疊中彈出一個值
                a = stack.pop() # 從堆疊中彈出一個值
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b)) # The division between two integers always truncates toward zero.捨去小數部分
                
            else:
                stack.append(int(token))
        return stack[0]
