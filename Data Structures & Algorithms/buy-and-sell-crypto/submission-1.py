class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        start = prices[0]

        for i in range(len(prices)):
            if prices[i] < start:
                start = prices[i]
            else:
                profit = prices[i] - start
                maxP = max(profit, maxP)
        return maxP



        