
class MyHashMap:

    def __init__(self):
        self.size = 10000
        # 初始化每個位置為空列表 [[], [], [], [], []]
        self.map = [[] for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        # self.map = [[], [], [], [[23, "A"]], [], [], [], [], [], []]
        # self.map = [[], [], [], [[23, "A"], [33, "B"]], [], [], [], [], [], []]
        index = key % self.size
        # 檢查鍵是否已存在
        for pair in self.map[index]: # index 是 3
            if pair[0] == key:   #23    #33
                pair[1] = value  #"A"   #"B"  若有新的[23, "A"]  key 23 已經存在，將value更新為 "C"
                return
        # 如果不存在，則加入新的鍵值對
        self.map[index].append([key, value])
        # 用([key, value])而不是Tuple ((key, value))是因為找到匹配的 key時，它會更新相應的value 如果用Tuple，當key存在時，就不能直接更新值了，而是需要創建一個新的元組來替換舊的元組  
        # List可變的 Tuple不可變的
        
    def get(self, key: int) -> int:
        index = key % self.size
        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]
        return -1
        
    def remove(self, key: int) -> None:
        index = key % self.size
        # enumerate 同時返回(pair) 和它們在該索引中的位置 (i) →　[23, "A"] return i=0  or [33, "B"]　return i=1
        for i, pair in enumerate(self.map[index]):
            if pair[0] == key:
                del self.map[index][i]
                return