class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Initialize stack with a 0
    
        for char in s:
            if char == '(':
                stack.append(0)  # Push 0 onto the stack for a new layer
            else:
                # Pop the top value of the stack and update the value below it
                popped = stack.pop()
                
                if popped == 0:  # For "()"
                    stack[-1] += 1
                else:  # For "(A)"
                    stack[-1] += 2 * popped
        
        return stack[0]