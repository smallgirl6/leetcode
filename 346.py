from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque() # 創建一個空的雙向隊列，作為MovingAverage對象的window屬性
        self.sum = 0 # 初始sum屬性

    def next(self, val: int) -> float:
        # 在MovingAverage對象的window尾部加一個整數val
        self.window.append(val)

        # 整數val加到MovingAverage對象的sum中
        self.sum += val

        # 若window中存的val數量已經超過一開始給定的size 3的話
        if len(self.window) > self.size:
            #從window的前端移除最早的整數並將這個整數從MovingAverage對象的sum中減去
            self.sum -= self.window.popleft()

# 返回sum除以window目前的長度，也就是移動平均值
        return self.sum / len(self.window)