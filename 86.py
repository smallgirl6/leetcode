class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize two dummy nodes and their corresponding pointers.
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before, after = before_dummy, after_dummy
        
        # Iterate through the list
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        # Connect the before list to the after list.
        before.next = after_dummy.next
        # Set the end of after list to None to prevent cycle in linked list
        after.next = None
        
        return before_dummy.next