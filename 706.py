class MyHashMap:

    def __init__(self):
        self.size = 10000
        # 初始化每個位置為空列表
        self.map = [[] for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 檢查鍵是否已存在
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # 如果不存在，則加入新的鍵值對
        self.map[index].append([key, value])
        
    def get(self, key: int) -> int:
        index = key % self.size
        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]
        return -1
        
    def remove(self, key: int) -> None:
        index = key % self.size
        for i, pair in enumerate(self.map[index]):
            if pair[0] == key:
                del self.map[index][i]
                return