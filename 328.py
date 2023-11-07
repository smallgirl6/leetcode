# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # 初始化odd和even指针
        odd = head
        even = head.next
        evenHead = even #不會移動，記住偶數節點的頭部，最把奇數部分的尾部和偶數部分的頭部連接起來。 
        #奇偶
        while even and even.next: #如果 even 或 even.next 是None，就等於走到最後了
            odd.next = even.next #將目前奇數位置的節點（odd）的 next 指向目前偶數位置節點（even）的下一個節點。 因為偶數位置節點的下一個節點是奇數
            odd = odd.next#　更新 odd 
            even.next = odd.next #將目前偶數位置的節點（even）的 next 指向目前奇數位置節點（odd）的下一個節點。 因為奇數位置節點的下一個節點是偶數
            even = even.next #更新even
            
        # 将奇数链表的末尾连接到偶数链表的头部
        odd.next = evenHead
        
        return head
