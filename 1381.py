        
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize # stack最大容量
        self.stack = []
        # 當新的元素被append stack時，self.top 的值會增加1，指向新的stack頂元素的位置；
        # 當元素被從stack中pop出時，self.top 的值會減少1，
        self.top = -1 # 第一個元素被append stack時會在0(-1+1)的位置
    # 將元素x加入stack中
    def push(self, x: int) -> None:
        # 如果stack還沒有達到最大容量 self.maxSiz
        if self.top < self.maxSize - 1:
            self.top += 1  # 將 stack頂指針top向上移一位
            self.stack.append(x) # 新元素 x 加到 self.stack 列表中
    # 將元素從stack中pop
    def pop(self) -> int:
        if self.top >= 0: # stack不為空 (不是-1)
            self.top -= 1 # 將 stack頂指針top向下移一位
            return self.stack.pop() # 取出並返回stack頂元素
        else: # stack為空，則返回-1
            return -1

    def increment(self, k: int, val: int) -> None:
        # 循環k和stack中元素個數的較小值次
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val # 將stack底的k個元素增加val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)