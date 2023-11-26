# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 如果 head 是空的或只有一個元素 或是旋轉次數 k 為 0
        if not head or not head.next or k == 0:
            return head
        
        # 先計算 linked list 的長度
        current, length = head, 0
        while current:
            length += 1
            current = current.next
        
        # 如果 k 的值大於鏈表的長度，那麼繼續旋轉就會回到它的原始狀態。例如，如果鏈表長度是 5，旋轉 5 次或 10 次，最終看起來都會和一開始一樣。
        k = k % length
        # 如果 k % length 的結果是 0， k 是鏈表長度的倍數，旋轉 k 次後鏈表會回到原來的狀態
        if k == 0:
            return head
        
        # 找到旋轉的起點
        # slow 和 fast 指針之間的固定距離（ k 步），當 fast 指到鏈表末尾時，slow 正好指向旋轉點
        slow, fast = head, head
        # head = [1,2,3,4,5], k = 2 fast ，指針向前移動 2 步，所以 fast 現在指向元素 3
        for _ in range(k): 
            fast = fast.next # 將 fast 指針向前移動 k 步

        # 同時移動 slow 和 fast 指針，每次都向前移動一步，直到 fast 指針到達鏈表的最後一個節點（ fast.next 為 None）
        # head = [1,2,3,4,5], k = 2。當 fast 指向元素 5 時，slow 將指向元素 3。
        while fast.next: # 開始同時移動 slow 和 fast 指針，每次都向前移動一步，直到 fast 指針到達鏈表的最後一個節點（ fast.next 為 None）
            slow, fast = slow.next, fast.next
        
        # 進行旋轉
        new_head = slow.next #  slow 指向元素 3，下一個元素（slow.next）是 4，成為旋轉後的新頭部。
        slow.next = None # ，slow 指向元素 3，將它的 next 設為 None，鏈表分為兩部分：一部分是 [1,2,3]，另一部分是 [4,5]。
        fast.next = head # 將這兩部分重新連接 fast現在指向鏈表的最後一個節點（元素 5），將 fast.next 設為原鏈表的頭部 head（指向元素 1）。
        
        return new_head