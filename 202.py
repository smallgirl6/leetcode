class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n,10) # n= 19 →　(new)n= 1, digit=9
                                        # n= 1  →  (new)n= 0, digit=1
                                        # n= 0  → break
                total_sum += digit ** 2 # digit=9*9 total_sum =81
                                        # digit=1*1 total_sum =81+1=82
            return total_sum

        seen = {} 
        while n != 1 and n not in seen: # 如果一個數字在過去已經出現過，那麼它將會造成無限循環，可以確定n  不是一個快樂數。
            seen[n] = True # 將數字 n 標記為已經看過
            n = next_num(n)     # return total_sum =82 => n=82  def next_num(82):

        return n == 1