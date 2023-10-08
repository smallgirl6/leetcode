# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 虛擬的頭節點
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            # 初始化節點
            first = current.next
            second = current.next.next
            
            # 交換
            first.next = second.next
            current.next = second
            second.next = first
            
            # 移動到下一個節點
            current = first
            
        return dummy.next
        