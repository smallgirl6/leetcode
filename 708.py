"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # 如果鏈表為空，創建一個新節點
        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        toInsert = False

        while True:
            # 當前值在兩個節點值之間
            if prev.val <= insertVal <= curr.val:
                toInsert = True
            # 在循環結尾
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            
            # 如果找到插入點，插入新節點
            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            
            prev, curr = curr, curr.next
            
            # 整個鏈表都已經遍歷
            if prev == head:
                break

        # 插入值大於或小於鏈表中所有值
        prev.next = Node(insertVal, curr)
        return head
        