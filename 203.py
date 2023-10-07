class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        creat_node = ListNode(0)     # 在頭前面做一個虛擬指標，防止要刪除的val是第一個
        creat_node.next = head       # 將虛擬指標後面接上head
        current = creat_node          # 創建一個current指針，並指向新節點
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return creat_node.next
