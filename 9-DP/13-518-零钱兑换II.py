from typing import *
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for co in coins:
            for j in range(co,amount+1):
                    dp[j]+=dp[j-co]
        print(dp)
        return dp[-1]