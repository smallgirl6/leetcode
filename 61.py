class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 如果 head 是空的或只有一個元素
        if not head or not head.next or k == 0:
            return head
        
        # 先計算 linked list 的長度
        current, length = head, 0
        while current:
            length += 1
            current = current.next
        
        # 計算實際要旋轉的次數
        k = k % length
        # 如果 k 是 0，表示不需要旋轉
        if k == 0:
            return head
        
        # 找到旋轉的起點
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow, fast = slow.next, fast.next
        
        # 進行旋轉
        new_head = slow.next
        slow.next = None
        fast.next = head
        
        return new_head