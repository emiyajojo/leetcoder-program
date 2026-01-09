from typing import *
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount==0: return 0
        if amount<min(coins): return -1
        
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for co in coins:
            for j in range(co,amount+1):
                dp[j]=min(dp[j],dp[j-co]+1)
        print(dp)
        dp[-1]=dp[-1] if dp[-1] != float('inf') else -1
        return dp[-1]