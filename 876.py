class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next: # 當 fast指針和fast 的下一個節點 不為 None 
            slow = slow.next      # slow指針指向下一個節點
            fast = fast.next.next # fast 指向下下個節點（移動兩個節點）
        return slow #返回 slow 指向的節點