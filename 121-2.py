class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0(n) / 0(1)
        no_stock = 0
        has_stock = end =-float('inf')

        for price in prices:
            tmp_no_stock = no_stock
            tmp_has_stock = has_stock
            has_stock = max(tmp_no_stock-price ,tmp_has_stock)
            end = max(tmp_has_stock + price ,end)
        return max(end,0)
