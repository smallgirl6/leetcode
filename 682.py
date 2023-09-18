class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total_sum = 0
        for op in operations:
            if op == "C":
                remove_last_num = stack.pop()
                total_sum -= remove_last_num
            elif op == "D":
                double_last_num = stack[-1] *2
                stack.append(double_last_num)
                total_sum += double_last_num
            elif op == "+":
                puls_last_2num = stack[-1]  + stack[-2]
                stack.append(puls_last_2num)
                total_sum += puls_last_2num
            else: # number
                new_num = int(op)
                stack.append(new_num)
                total_sum += new_num
        return total_sum 
