# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 從 list1 中移除從第 a 個節點到第 b 個節點的部分。然後，將 list2 插入到這個位置。
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
       # 初始化一個指針，從 list1 的頭部開始
        current = list1

        # 找到第 a-1 個節點　list1 = [0,1,2,3,4,5], a = 3
        # 　　　　　　　　　　　　　　　　  ＾　　　　
        for i in range(a - 1):
            current = current.next
        # 保存第 a-1 個節點 
        first_part = current

        # 從當前位置（第 a-1 個節點）移動到第 b+1 個節點 list1 = [0,1,2,3,4,5], a = 3 b = 4
        #                                                          ＾  ＾                                                    
        for i in range(b - a + 2): # b+1 - (a-1)
            current = current.next
        # 保存第 b+1 個節點
        second_part = current

        # 將第 a-1 個節點的 next 指向 list2 的頭部
        first_part.next = list2

        # 遍歷到 list2 的末尾
        while list2.next:
            list2 = list2.next

        # 將 list2 的末尾與第 b+1 個節點連接
        list2.next = second_part

        # 返回合併後的鏈表的頭部
        return list1

