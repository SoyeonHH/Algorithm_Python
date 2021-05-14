import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)   # 최솟값 갱신
            profit = max(profit, price - min_price) # 최댓값 갱신
        return profit