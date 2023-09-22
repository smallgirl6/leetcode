# s = "()()" 就是 A="()" 和 B="()" ，AB = "()()"，score是 1 + 1 = 2。
# s = "(())" 就是 A="()"  (A)，score是 2 *1 = 2。
# s = "(()())"，score是 2 *2 = 4。
# s = "(()(()))" ，score是 2 *3 = 6。
#   stack = [0] 
# ( stack = [0, 0]
# (( stack = [0, 0, 0]
# (()  stack = [0, 1] * pop 0 ， stack[-1] += 1
# (()(  stack = [0, 1, 0]
# (()((  stack = [0, 1, 0, 0] * pop 0 ， stack[-1] += 1
# (()(()  stack = [0, 1, 1]
# (()(()) stack = [0, 3 ] * pop 1  ， stack[-1] += 2 * 1
# (()(()))  stack = [6] * pop 3  ，stack[-1] += 2 * 3

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else: # char == ")"
                popped = stack.pop()
                if popped == 0:   # "()" ， (()  stack = [0, 1] * pop 0 ， stack[-1] += 1
                    stack[-1] += 1
                else:  # (()) ，(()(()) stack = [0, 3 ] * pop 1  ， stack[-1] += 2 * 1
                    stack[-1] += 2 * popped
        return stack[0]
