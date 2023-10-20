class MyCircularDeque:
    # front, rear = -1, -1 [_, _, _, _] 
    # front, rear = 0, 0   [A, _, _, _]  在rear處插入A
    # front, rear = 0, 1   [A, B, _, _]  在rear處再插入B
    # front, rear = 0, 2   [A, B, C, _]  在rear處再插入C
    # front, rear = 0, 3   [A, B, C, D]  在rear處再插入D # rear指針的下一個位置將是0

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k # queue: [None, None, None]
        self.front = self.rear = -1 # 當 self.front 和 self.rear 都為 -1 時，表示這個隊列是空的
        # 初始化queue時，不知道第一個元素會插入前端或尾端，因此一開始把 front 和 rear 都設為 -1 。

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty(): # 當第一個元素被插入時，不論是插入到前端還是尾端，front 和 rear 都會被設定為 0
            self.front = self.rear = 0 
        else:
            self.front = (self.front - 1) % self.size # rear指針向左移動一位。如果front 指針已經在隊列的第一位，它會回到隊列的最後一位。
        self.queue[self.front] = value # 將指定的 value 存儲到循環隊列中 front 指針當前指向的位置
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():  # 當第一個元素被插入時，不論是插入到前端還是尾端，front 和 rear 都會被設定為 0
            self.front = self.rear = 0  
        else:
            self.rear = (self.rear + 1) % self.size # rear指針向右移動一位。如果rear指針已經在隊列的最後一位，它會回到隊列的起始位置。
        self.queue[self.rear] = value # 將指定的 value 存儲到循環隊列中 rear 指針當前指向的位置
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:    # 如果 front 和 rear 指向同一位置，則queue只有一個元素
            self.front = self.rear = -1 # 當刪除這個元素後，queue將變為空，需要重置 front 和 rear 指針到 -1 
        else:
         # 將 self.front 指針移動到下一個元素。原本前端的元素現在被"忽略"或"刪除"了，
         # 即使它在數組中仍然存在。如果後續有新的元素插入，這個被"忽略"的元素可能會被覆蓋。
            self.front = (self.front + 1) % self.size 
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear: # 如果 front 和 rear 指向同一位置，則queue只有一個元素
            self.front = self.rear = -1 # 當刪除這個元素後，queue將變為空，需要重置 front 和 rear 指針到 -1 
        else:
            self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        # self.front 的值為 -1，則隊列是空的。因為在初始狀態和每次從隊列中刪除所有元素之後，self.front 和 self.rear 都會被設置為 -1
        return self.front == -1

    def isFull(self) -> bool:
        # rear指針的下一個位置將是0 代表queue已經滿了
        return (self.rear + 1) % self.size == self.front
        

 

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()