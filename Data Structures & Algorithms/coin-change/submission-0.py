class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

        #dp[0]=0 dp[1]=1 dp[2]=2 dp[3]=3 dp[4]=4 dp[5]=1 dp[6]=2 dp[7]=7 dp[8]=8 dp[9]=9 dp[10]=10 dp[11]=11 dp[12]=12 