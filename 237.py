# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node不應該是清單的最後一個節點，而應該是清單中的實際節點
        # node 存在(不是 None)， node 有一個下一節點( next 不是 None)
        if node and node.next:
            # node的值(val)設定為其下一個節點(node.next)的值
            # 當前節點的值替換為其下一個節點的值    
            node.val = node.next.val
            # 將當前節點node的下一個節點next設定為其下一個節點的下一個節點
            # 前節點跳過其直接的下一個節點，直接連接到下下個節點
            node.next = node.next.next