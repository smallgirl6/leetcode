class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []  # 存目前為止的最小元素

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]: # min_stack是空的 or 新加入的值val小於或等於當前的最小值
            self.min_stack.append(val) # val將被加入到min_stack中

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]: 
            # self.stack的頂部元素（也就是我們即將移除的元素）是否等於self.min_stack的頂部元素
            # 如果是，則要移除的元素是當前的最小元素，所以也需要從self.min_stack中移除它。
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

