class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 創建一個虛擬的頭節點，這將使處理邊界情況更容易。
        sentinel = ListNode(0)
        sentinel.next = head
        
        current = sentinel
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return sentinel.next