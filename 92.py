# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: # left == right代表指向同一個位置(鏈表中只有一個值)
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy # prev的初始是在0(鏈表的虛擬dummy開頭)
        
        # 找出要從哪裡開始轉換(left)的前一個值 [1,2,3,4,5] 的話就是1
        for _ in range(left - 1):
            prev = prev.next # 一直向前移直到left前一個位置就停
        
        # Reverse the sublist
        current = prev.next  # current指針指向prev的下一個 就是要開始翻轉的位置left
        # head = [1,2,3,4,5]
        #         p c
        for _ in range(right - left):
            next_node = current.next  # next_node代表current指針的下一個  current是2的話 current.next就是3 next_node = 3
                                        ##二次迭代  current=2 current.next=4  next_node 指向4
            current.next = next_node.next # current.next指向next_node.next  next_node.next = 4 current.next指向4  # 把2指向4
                                                                                               #  [1,2,4,5] 2的下一個指向4 3目前懸浮著
                                                                                               #       3

                                        ##二次迭代  next_node.next=5  current.next current.next 2下一個5 把2指向5 # [1,3,2,5]  4目前懸浮著
                                                                                                                       # 4
            next_node.next = prev.next # 懸浮的3的下一個指向left前一個位置的下一個位置      # 把3指向2       
                                       ##二次迭代  懸浮的4的下一個指向left前一個位置的下一個位置      # 把4指向3 
            prev.next = next_node      # prev.next left前一個位置的下一個位置指向 next_node 3  把1指向3。    #  [1,3,2,4,5]
                                       ##二次迭代 prev.next left前一個位置的下一個位置指向 next_node 4  把1指向4。#  [1,4,3,2,5]

        return dummy.next

