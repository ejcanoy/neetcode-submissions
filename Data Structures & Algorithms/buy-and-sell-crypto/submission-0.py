class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for val in prices:
            maxProfit = max(maxProfit, val - minPrice)
            if val < minPrice:
                minPrice = val
        return maxProfit
