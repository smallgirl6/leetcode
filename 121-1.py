class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit  = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit