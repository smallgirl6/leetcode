"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#RECURSION  
#先訪問根節點在訪問子節點
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = [] # = result=[root.val]
        result.append(root.val)
        for child in root.children:
            result.extend(self.preorder(child))
        return result#RECURSION  
