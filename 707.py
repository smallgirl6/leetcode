class MyLinkedList:

    def __init__(self):
        self.head = [None, None]  # 初始化頭節點，包含值為 None 和下一個節點的引用為 None
        self.size = 0  # 初始化鏈表的大小為 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: # index小於0 或 小於等於初始化鏈表的大小則索引無效
            return -1                       # 返回 -1
        current = self.head                 # current 被設置為鏈表的頭節點
        # 在每次迭代中，current 會被更新為它的下一個節點，即 current[1]。
        # 這樣，當迴圈結束時，current 會指向索引為 index 的節點。
        for _ in range(index + 1):
            current = current[1]  # 遍歷鏈表直到達到指定索引

        # 最後返回該節點的值，即 current[0]。
        # 在這個實現中，鏈表的節點表示為包含兩個元素的列表：
        # 第一個元素（索引為 0）是節點的值，第二個元素（索引為 1）是對下一個節點的引用。
        return current[0]  # 返回指定索引的節點值

    def addAtHead(self, val: int) -> None:
        # 第一個元素（索引為 0）是 val，為節點的值；第二個元素（索引為 1）是對原始頭節點的引用
        self.head[1] = [val, self.head[1]]  # 將新節點插入到頭部，並將其下一個節點的引用指向原始頭部
        self.size += 1  # 添加了新節點所以更新鏈表大小

    def addAtTail(self, val: int) -> None:
        current = self.head       #將 current 設置為鏈表的頭節點
        while current[1]:         # 如果 current 節點的下一個節點存在
            current = current[1]  # 將 current 更新為下一個節點current[1]
        current[1] = [val, None]  # 在尾部添加新節點，下一個節點的引用為 None
        self.size += 1            # 添加了新節點所以更新鏈表大小

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: # index小於0 或 小於初始化鏈表的大小則索引無效
            return                         # 如果索引無效，則不插入節點
        current = self.head                # current 被設置為鏈表的頭節點
        # 在每次迭代中，current 會被更新為它的下一個節點，即 current[1]
        for _ in range(index):
            current = current[1]           # 遍歷鏈表直到達到指定索引的前一個節點
        current[1] = [val, current[1]]     # 將新節點插入到指定索引的位置
        self.size += 1                     # 更新鏈表大小

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: # index小於0 或 小於等於初始化鏈表的大小則索引無效
            return                         # 如果索引無效，則不刪除節點
        current = self.head                # current 被設置為鏈表的頭節點
         # 在每次迭代中，current 會被更新為它的下一個節點，即 current[1]
        for _ in range(index):   
            current = current[1]           # 遍歷鏈表直到達到指定索引的前一個節點
        # current[1][1]指定索引節點（即要刪除的節點）的下一個節點的引用。
        current[1] = current[1][1]         # 刪除指定索引的節點
        self.size -= 1                     # 更新鏈表大小

