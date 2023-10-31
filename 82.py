# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化 dummy node 和 prev node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            # 如果當前節點有下一個節點且其值與下一個節點的值相同，則跳過所有重複的節點
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next  # 移除所有重複的節點
            else:
                prev = prev.next  # 如果當前節點沒有重複，則移動 prev 到當前節點
            head = head.next  # 移動到下一個節點

        return dummy.next  # 回傳已移除重複節點的連結串列的頭節點