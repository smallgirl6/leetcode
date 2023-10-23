# recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 創建一個遞歸函數，返回反轉後的新節點
        def recr(node):
            # 如果節點為空或只有一個節點，直接返回節點
            if not node or not node.next:
                return node
            
            # 遞歸獲取節點的下一個節點
            # head = [1,2,3,4,5]  
            # node =1  node.next =2 反轉從2開始的鏈表 2 -> 3 -> 4 -> 5 會被反轉為 5 -> 4 -> 3 -> 2。  next_node 現在是 5
            next_node = recr(node.next) #  recr(2)，然後 recr(3)... recr(5)
            # node.next.next 2的下一個指針指向當前節點 node (node =1 ) 
            node.next.next = node
            # 斷開當前節點與下一個節點之間的連接 斷開了 1 和它原本的下一個節點之間的連接
            node.next = None 
            # 返回下一個節點 返回反轉後的鏈表的開頭，即 5。
            return next_node 
        
        # 調用遞歸函數，傳入頭節點，返回反轉後的新節點
        return recr(head)