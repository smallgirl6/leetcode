class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i = 0  # index for target
        for num in range(1, n+1):
            if i >= len(target):
                break  # we have built the target array, so stop
            
            # Push the current number to the stack
            result.append("Push")
            
            if num == target[i]:
                i += 1  # move to the next element in target
            else:
                # The current number doesn't match the target, so pop it
                result.append("Pop")
        
        return result