# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_point = head
        while current_point and current_point.next: # # 確保當前節點和下一個節點都存在
            if current_point.val == current_point.next.val:
                current_point.next = current_point.next.next
            else:
                current_point = current_point.next
        return head
            