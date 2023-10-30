# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
    
        # Push all elements of l1 into s1
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        # Push all elements of l2 into s2
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while s1 or s2 or carry:
            sum_val = carry

            if s1:
                sum_val += s1.pop()

            if s2:
                sum_val += s2.pop()

            carry = sum_val // 10
            node = ListNode(sum_val % 10)

            # Add node to the front of the result list
            node.next = head
            head = node

        return head
        