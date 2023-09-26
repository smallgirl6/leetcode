# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = self.tail = -1
        self.size = k
        self.current_size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():  # 隊列已滿，則無法入隊
            return False
        if self.isEmpty(): # 隊列為空，則更新頭部索引
            self.head = 0
        self.tail = (self.tail + 1) % self.size # 更新尾部索引
        self.queue[self.tail] = value # 在尾部位置添加元素
        self.current_size += 1  # 更新當前元素數量
        return True  # 入隊成功

    def deQueue(self) -> bool:
        if self.isEmpty(): # 如果隊列為空，則無法出隊
            return False
        if self.head == self.tail: # 頭尾索引相同，則隊列中只有一個元素
            self.head = self.tail = -1  # 移除唯一的元素後，重置頭尾索引
        else:
            self.head = (self.head + 1) % self.size  #更新頭部索引
        self.current_size -= 1  # 更新當前元素數量
        return True # 出隊成功

    def Front(self) -> int:
        if self.isEmpty(): #  隊列為空，則返回-1
            return -1
        return self.queue[self.head]  # 返回頭部元素

    def Rear(self) -> int:
        if self.isEmpty(): #  隊列為空，則返回-1
            return -1
        return self.queue[self.tail] # 返回尾部元素

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.size