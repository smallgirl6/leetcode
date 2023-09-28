class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for index, char in enumerate(s):
            if char == "(":
                left_stack.append(index)
            elif char == "*":
                star_stack.append(index)
            else: # char = ")"
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else: 
                    return False
        while left_stack:
            if not star_stack:
                return False
            if star_stack[-1] > left_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                return False
        return True