# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        # [dummy, 1, 2, 3, 4]
        #    ^ 
        #  current
        while current.next and current.next.next:
            first = current.next        # 1
            second =  current.next.next #  2

            first.next = second.next # 2 <= 3
            current.next = second  # 1 <= 2 
            second.next = first     # 3 <= 1 

            # 移動到下一個節點
            current = first
        
        return dummy.next
        