class MyStack:

    def __init__(self):
        self.q1 = []  # 主queue
        self.q2 = []  # 輔queue

    def push(self, x: int) -> None:
        self.q1.append(x) # 新元素推入q1

    def pop(self) -> int:
        # 如果q1是空的，那麼stack就是空的，我們不能彈出任何東西
        if not self.q1:
            return None

        # 把q1中的元素，除了最後一個以外，全部移到q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        
        # 彈出q1中的最後一個元素，這就是答案
        top_val = self.q1.pop(0)
        
        # 交換q1和q2，這樣q1又回到了主隊列的位置
        self.q1, self.q2 = self.q2, self.q1
        
        return top_val

    def top(self) -> int:
        if not self.q1:
            return None
        
        return self.q1[-1]  # 返回q1的最後一個元素，但不從其中移除它

    def empty(self) -> bool:
        return not self.q1  # 如果stack是空的，則堆疊是空的