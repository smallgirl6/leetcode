# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # 初始化odd和even指针
        odd = head
        even = head.next
        evenHead = even
        
        # 遍历链表
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        # 将奇数链表的末尾连接到偶数链表的头部
        odd.next = evenHead
        
        return head
        