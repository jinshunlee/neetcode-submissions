class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSum = 0
        r = 1
        l = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxSum = max(maxSum, profit)
                r += 1
            else:
                l = r
                r += 1
        return maxSum



            

        