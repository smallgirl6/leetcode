# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1　=> [1]
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2 => [1,100]
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3 => [1,100,3001]
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3 => 2~3002 [100,3001,3002]

class RecentCounter:
    def __init__(self):
        self.requests = [] # 使用一個列表來存儲所有ping的時間戳

    def ping(self, t: int) -> int:
        self.requests.append(t) # 每次調用ping方法時，將時間戳記t添加到列表中　1　　[1]
                                                                         # 100　[1,100]
                                                                         # 3001 [1,100,3001]
                                                                         # 3002 [1,100,3001,3002]

        # 遍歷列表中的請求，刪除所有過期(所有時間戳小於等於 t - 3000 的元素，
        # 因為它們已經不在最近一段時間內)的請求時間戳
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
                                                            #  t=1 => 1 < 1-3000 =>　nopop  [1]
                                                            #  t=100 => 1 < 100-3000　nopop [1]
                                                            #           100 < 100-3000 nopop[1,100]
                                                            #  t=3001 => 1 < 3001-3000　nopop  [1]
                                                            #           100 < 3001-3000 nopop [1,100]
                                                            #           3001 < 3001-3000 nopop[1,100,3001]
                                                            #  t=3002 => 1 < 3002-3000(2)　pop  []
                                                            #           100 < 100-3000 nopop [100]
                                                            #           3001 < 3001-3000 nopop[100,3001]
                                                            #           3002 < 3002-3000 nopop[100,3001,3002]
        return len(self.requests) # 返回最近一段時間內的請求次數
        