class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # 初始化結果列表 [0,0,0,0....]
        stack = []  # 堆疊存儲氣溫的索引
        for index, temperature in enumerate(temperatures):  # 遍歷每一天的氣溫
            while stack and temperatures[stack[-1]] < temperature:  # 目前氣溫比stack頂部天氣溫高
                stack_up_index = stack.pop()  # 彈出stack頂部索引
                res[stack_up_index] = index - stack_up_index  # 計算天數差並存儲到結果列表
            stack.append(index)  # 目前的氣溫的索引入stack
        # stack中剩餘的索引對應的結果已經初始化為0，不需要再次設置
        return res  # 返回結果列表