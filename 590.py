"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# root = [1,null,3,2,4,null,5,6]
# stack = [1,4,2,3,6,5]
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not  root:
            return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            # print(root.val)
            result.append(root.val)
            stack.extend(root.children)
        # print(result)
        return reversed(result) # result[::-1]