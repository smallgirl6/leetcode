# 使用兩個stacks來實現一個queue

class MyQueue:

    def __init__(self):
        # Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
    #如果 s2 是空的，需要從 stack1 的頂部彈出所有元素並加入到 stack2 反轉 stack1 中的元素順序。最早加入的元素在 stack2 的頂部，可以被直接訪問
    def pop(self) -> int:
        # 如果 s2 是空的，當 s1 不是空的時，從 s1 彈出一個元素並推入 s2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # 從 s2 彈出頂部的元素
        return self.stack2.pop()

    def peek(self) -> int: # 查看QUEUE或STACK的頂部元素，但不從QUEUE或STACK中移除它
    # 如果 s2 是空的，當 s1 不是空的時，從 s1 彈出一個元素並推入 s2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # 從 s2 查看頂部的元素
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
