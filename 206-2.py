# iteration
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # 反轉的開始，沒有"上一個節點"，所以是None
        current = head #頭開始進行反轉。 head = [prev,1,2,3,4,5]  
        
        while current: #只要還沒有到達鏈表的結尾，循環就會運行
            # 保存當前節點的下一個節點  next_node = current.next 1的下一個就是2  next_node =2
            next_node = current.next
            # 將當前節點指向prev 將1的下一個指針指向prev(None) 1,prev
            current.next = prev
            # 更新prev為當前節點 將prev變成1
            prev = current
            # 移動到下一個節點  將current變2( next_node =2)
            current = next_node
        # 當循環結束時，current 是 None（因為已經遍歷完整個鏈表），而 prev 指向的是反轉後的鏈表的開始，因此返回 prev 就等於返回反轉後的鏈表。
        return prev
