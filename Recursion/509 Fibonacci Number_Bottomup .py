class Solution:
    def fib(self, n: int) -> int:
        # 若要計算第0項則返回0
        if n == 0:
            return 0
        # 若要計算第1項則返回1
        elif n == 1:
            return 1
        # 否則把前兩項的和計算出來放到result
        result =self.fib(n-1) + self.fib(n-2)
        # 返回结果
        return result
    
# 創建 Solution 類的一個實例
solution_instance = Solution()
# 通過實例調用 fib 函數
fib_result = solution_instance.fib(8)

print(fib_result)