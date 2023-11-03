class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # 創建一個虛擬節點當作返回的新鏈表的頭
        ptr = dummy         # 指針ptr指向新鏈表的虛擬頭節點
        
        while list1 and list2:         # list1 and list2都不為空就跑循環
            if list1.val <= list2.val: # 如果list1當前節點的值小於等於list2當前節點的值
                ptr.next = list1       # 新鏈表的指針ptr的下一個節點指向list1當前節點
                list1 = list1.next     # list1的指針移動到list1下一個節點
            else:                      # 如果list1當前節點的值大於list2當前節點的值
                ptr.next = list2       # 新鏈表的指針ptr的下一個節點指向list2當前節點
                list2 = list2.next     # list2的指針移動到list2下一個節點
                
            ptr = ptr.next # 將指針ptr移動到下一個節點
        
        if list1: # 如果list1還有剩餘的節點
            ptr.next = list1 # 新鏈表的指針ptr的下一個節點指向list1的剩餘節點
        if list2: # 如果list2還有剩餘的節點
            ptr.next = list2 # 新鏈表的指針ptr的下一個節點指向list2的剩餘節點
            
        return dummy.next # 返回新的鏈表的頭節點