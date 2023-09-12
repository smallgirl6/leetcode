class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total_sum = 0  # 初始化總得分為0
        
        for op in operations:
            if op == 'C':
                # 取消前一個得分
                last_score = stack.pop()
                total_sum -= last_score
            elif op == 'D':
                # 前一個得分的兩倍
                new_score = stack[-1] * 2
                stack.append(new_score)
                total_sum += new_score
            elif op == '+':
                # 前兩個得分的總和
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
                total_sum += new_score
            else:
                # 這是一個整數，直接加到得分裡
                new_score = int(op)
                stack.append(new_score)
                total_sum += new_score
        
        return total_sum