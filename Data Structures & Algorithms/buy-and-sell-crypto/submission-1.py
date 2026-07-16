class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_prof = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r += 1
            else:
                if profit > max_prof:
                    max_prof = profit
                r += 1
        
        return max_prof
                

        