"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Helper function to flatten the multilevel linked list using DFS.
        def dfs(node):
            curr = node
            last = None  # keeps track of the last visited node in the DFS
            
            while curr:
                next_node = curr.next  # store the next node
                if curr.child:
                    # Flatten the child list
                    child_last = dfs(curr.child)
                    
                    # Connect current node to the start of the child list
                    next_node = curr.next
                    curr.next = curr.child
                    curr.child.prev = curr
                    
                    # Connect the end of the child list to the next node
                    if next_node:
                        child_last.next = next_node
                        next_node.prev = child_last
                    
                    # Set child pointer to null
                    curr.child = None
                    last = child_last
                else:
                    last = curr
                curr = next_node
            
            return last  # return the last node of the flattened list
        
        dfs(head)
        return head