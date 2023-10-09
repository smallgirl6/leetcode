class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        # 先讓 fast 移動 n+1 步
        #  n+1 步而不是 n 步是因為，希望fast走到最後 second 指針能夠指向要刪除節點的前一個節點
        for i in range(n+1):
            fast = fast.next

        # 一起往前移動直到fast到最後
        # slow 指針將位於從末尾數來的第 n+1
        while fast:
            fast = fast.next
            slow = slow.next
        # slow 指針的下一個節點是要刪除的節點
        slow.next = slow.next.next
        return dummy.next