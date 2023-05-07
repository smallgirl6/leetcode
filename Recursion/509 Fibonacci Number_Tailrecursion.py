class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: # 輸入的 n 小於等於 1，則直接返回 n 
            return n # (n == 0(1) return 0(1) )
        a,b = 0 ,1 # 否則初始化變量 a 和 b 分別為 0 和 1
        for i in range(n-1): # for 循環來計算斐波那契數列的第 n 項
            c = a+b          # 每次將 a 和 b 相加得到c 
            a = b            # a 賦值為 b
            b = c            # b 賦值為 c
        return b             # 返回變量 b()斐波那契數列的第 n 項)
    
# 創建 Solution 類的一個實例
solution_instance = Solution()
# 通過實例調用 fib 函數
fib_result = solution_instance.fib(7)

print(fib_result)