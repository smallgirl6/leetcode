class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Define the State class locally
        class State:
            def __init__(self, current_string, left_count, right_count):
                self.current_string = current_string
                self.left_count = left_count
                self.right_count = right_count

        if n == 0:
            return []
        
        result = []
        queue = deque([State("", 0, 0)])
        
        while queue:
            current_state = queue.popleft()
            
            if current_state.left_count == n and current_state.right_count == n:
                result.append(current_state.current_string)
                continue
            
            if current_state.left_count < n:
                queue.append(State(
                    current_state.current_string + "(",
                    current_state.left_count + 1,
                    current_state.right_count
                ))
            
            if current_state.right_count < current_state.left_count:
                queue.append(State(
                    current_state.current_string + ")",
                    current_state.left_count,
                    current_state.right_count + 1
                ))
        
        return result