class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #  Since the answer may be large, return the answer modulo 10**9 + 7.大質數
        MOD = 10**9 + 7
        stack = [] # 保持一個由小到大的順序，記錄那些還沒被當前數字“覆蓋”的數字
        ans = 0
        dot = 0  #  目前這個數字為止，所有的子陣列的最小值之和
    # [3, 7, 2]：
    #當元素 3，只有子陣列 [3] 是以 3 結尾且 3 是最小的。所以，dot = 3 * 1 = 3。
    #當元素 7，只有子陣列 [7] 是以 7 結尾且 7 是最小的。所以，dot = 7 * 1 = 7。
    #當元素 2，有三個子陣列是以 2 結尾且 2 是最小的，分別是 [2]、[7, 2] 和 [3, 7, 2]。所以，dot = 2 * 3 = 6。

        for i, num in enumerate(arr):
            count = 1  # 最小值的子陣列的數量  這個數字至少能夠形成它自己這一個子陣列所以至少有1個
                       # 前數字左邊比它大的連續數字的數量 + 1。比如說[5,5,5,2]，對於數字2，前面有三個5比它大，所以count=4
            # stack[-1][0]：取得那個元組的第一個元素，即數字
            # stack = [(3, 2), (5, 1), (7, 1)] stack[-1] 是 (7, 1)，而 stack[-1][0] 是 7
            while stack and stack[-1][0] >= num:  # 移除 stack 頂部所有小於或等於當前元素的元素
                val, cnt = stack.pop() #若 stack 現在是 [(3, 2), (5, 1)] stack.pop() 將返回 (5, 1)  val=5, cnt=1
                count += cnt  # 更新 count 為從當前元素到前一個比它小的元素的距離
                dot -= val * cnt  # 更新 dot 陣列最小值由之前的數字變成了當前的數字

            stack.append((num, count))  # 將當前元素和 count 加入 stack
            dot += num * count  # 更新 dot
            ans = (ans + dot) % MOD  # 更新答案

        return ans