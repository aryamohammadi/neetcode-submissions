class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxp = 0
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            profit = prices[R] - prices[L]
            maxp = max(maxp, profit)
        return maxp
