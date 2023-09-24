"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# DFS stack LIFO
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        output = []
        stack = [root]
        
        # [1,null,3,2,4,null,5,6]
        # stack = [1]， ouput = [1] → output.append(current.val) ， stack = [3,2,4] extend reversed stack = [4,2,3]
        # stack = [4,2,3] →pop(LIFO) 3 output = [1,3] ， 
        #                              3的孩子(5,6)加入原有剩下4和2的stack 
        #                                                stack = [4,2,5,6] extend reversed stack = [4,2,6,5]
        #                           →5 output = [1,3,5] ， stack = [4,2,6]
        #                           →6 output = [1,3,5,6] ， stack = [4,2]                      
        #                           →2 output = [1,3,5,6,2] ， stack = [4]
        #                           →4 output = [1,3,5,6,2,4] ， stack = []

        while stack:
            current = stack.pop()
            output.append(current.val) 
            stack.extend(reversed(current.children))
        return output
            
# current.children = [child1, child2, child3]，
# reversed(current.children) => [child3, child2, child1]