class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base case
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        # Find the middle node using slow and fast pointer approach
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        if prev:
            prev.next = None  # Break the linked list into two halves

        # Create the root node with the value of the middle node
        root = TreeNode(slow.val)
        
        # Recursively build the left and right subtree
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root
        