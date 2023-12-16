# Definition for singly-linked list.
# 單向鏈表節點的定義。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點值
        self.next = next  # 指向下一個節點

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果鏈表為空或只有一個節點，則不需要排序
        if not head or not head.next:
            return head

        dummy = ListNode(0)  # 創建一個虛擬頭節點，方便處理邊界情況
        current = head  # 從頭節點開始處理

        # 遍歷鏈表中的每個節點
        while current:
            # 從虛擬頭節點開始，找到當前節點應該插入的位置
            prev = dummy
            # 如果 prev.next 是 None，表示 prev 已經是鏈表的最後一個節點
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # 將當前節點插入到已排序的部分
            temp = current.next  # 暫存當前節點的下一個節點
            current.next = prev.next
            prev.next = current

            # 移動到下一個待處理的節點
            current = temp

        # 返回排序後的鏈表頭節點
        return dummy.next

        