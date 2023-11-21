#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 計算鏈表的長度
        length, current = 0, head
        while current: # 計算鏈表的長度
            length += 1
            current = current.next
        
        # 計算每個部分的基本長度和需要額外增加一個節點的部分數量
        part_size, extra = divmod(length, k) # head = [1,2,3,4,5,6,7,8,9,10], k = 3   10/3 = 3...1
        # part_size 每個部分的基本長度 extra 餘下的節點數 #  part_size =3  extra= 1 
        # 分割鏈表
        result = [None] * k  #result = [None, None, None]
        current = head # 重置 current 為 head 不然剛剛current = head 已經跑到最後了
        for i in range(k):
            # 建立新鏈表的頭節點
            result[i] = current # 將目前節點 current 設定為第 i 部分的頭節點
            current_size = part_size + (1 if i < extra else 0)
            # 計算目前部分的大小。 part_size 是鍊錶平均分割的大小，而 extra 是用來處理不能均勻分割的情況，給前幾部分多分配一個節點。
            # 對於[1,2,3,4]（i = 0），current_size 是 3 + 1 = 4，因為 0 < 1（extra）。
            # 對於[5,6,7],[8,9,10]（i = 1 和 i = 2），current_size 是 3，因為 1 和 2 不小於 1（extra）。 
            # 內部遍歷 [1,2,3,4]
            for j in range(current_size - 1):
                if current:
                    current = current.next
            if current:
                # 斷開與下一部分的連接 [1,2,3,4]要到[5,6,7]這一個part
                next_part = current.next
                current.next = None
                current = next_part

        return result
