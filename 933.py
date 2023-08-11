class RecentCounter:
    def __init__(self):
        self.requests = [] # 使用一個列表來存儲所有ping的時間戳

    def ping(self, t: int) -> int:
        self.requests.append(t) # 每次調用ping方法時，將時間戳記t添加到列表中
        
        # 遍歷列表中的請求，刪除所有過期(所有時間戳小於等於 t - 3000 的元素，
        # 因為它們已經不在最近一段時間內)的請求時間戳
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        
        return len(self.requests) # 返回最近一段時間內的請求次數