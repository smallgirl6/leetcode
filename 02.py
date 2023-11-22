#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        ptr = dummy            # 指針ptr指向虛擬節點
        carry = 0              #  carry表示進位，初始化為0
        
        while l1 or l2:        # 遍歷l1和l2
            #val1和val2為 l1和l2當前節點的值，如果節點為空則值為0
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0
            # 將當前節點的值和進位的值相加
            total = val1 + val2 + carry

             # 判斷是否進位
            if total >= 10:
                carry = 1    # carry 更新為１
                total -= 10  #　total-10
            else:            #　沒進位
                carry = 0    #　carry為0
            
            # 將當前位的值插入新的節點中，並將ptr指針指向新的節點
            ptr.next = ListNode(total) # 在鏈表中添加一個新的節點，計算結果。
            ptr = ptr.next

            # 將l1和l2的指針指向下一個節點
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 最後判斷是否有進位，如果有，再新建一個節點        
        if carry != 0:
            ptr.next = ListNode(carry) 
        # 返回虛擬節點的下一個節點，即新鏈表的頭節點    
        return dummy.next