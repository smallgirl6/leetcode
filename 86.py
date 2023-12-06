# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 建構兩個分區：包含小於 x 的節點，包含大於或等於 x 的節點
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before, after = before_dummy, after_dummy # 兩個指針

        while head:
            if head.val < x:
                # 節點的值小於 x，加入到 before 鏈表   [1,2,2]
                before.next = head
                before = before.next
            else: # 節點的值大於 x，加入到 after 鏈表   [4,3,5]
                after.next = head
                after = after.next
            head = head.next
        # 完成遍歷後，將 before 的最後一個節點連接到 after_dummy.next
        before.next = after_dummy.next
        #  after 鏈表的末尾設為 None
        after.next = None
        
        return before_dummy.next