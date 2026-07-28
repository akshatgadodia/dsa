class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in (prices[1:]):
            profit = i - min_price
            if profit > max_profit:
                max_profit = profit
            if i < min_price:
                min_price = i

        return max_profit

