class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0(n) / 0(n) -where n is length of price
        # dp[i] = 0~i  最小price
        n = len(prices)
        dp = [float('inf')] * n
        dp[0] = prices[0]
        ans = 0
        for i in range(1,n):
            price = prices[i]
            dp[i] = min(dp[i-1],price)

            ans = max(ans,price - dp[i-1])
        return ans