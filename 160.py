# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         if not headA or not headB:
#             return None
        
#         a, b = headA, headB
        
#         while a != b:
#             a = a.next if a else headB
#             b = b.next if b else headA
        
#         return a
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: # 其中一個List沒有值，不可能有相交節點
            return None
        a = headA
        b = headB

        while a != b: # 兩個指標以相同的步長遍歷兩個鏈表的所有節點。如果指向的節點相同，則找到了相交節點，兩個指標都為None，即兩個鍊錶不相交
            if a: #如果a非空，就讓 a 移動到下一個節點 a.next。
                a = a.next
            else: # 如果a為None（已到達鍊錶末端），則將a重設為鍊錶B的頭節點。 這樣做是為了抵消兩個鍊錶長度的差異。
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a  # a == b  回傳b也可以 反正後面都一樣