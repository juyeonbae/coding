class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n+1)

        j, mx = 0, 0
        for i in range(1, n):
            dp[i-1] = max(mx, prices[i] - prices[j])
            if prices[j] > prices[i]:
                j = i 
        
        return max(dp)
