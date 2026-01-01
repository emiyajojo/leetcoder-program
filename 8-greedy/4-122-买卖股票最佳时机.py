from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            res+=max(0,prices[i]-prices[i-1])
        return res

pri=[1,2,3,4,5]
sol=Solution()
print(sol.maxProfit(pri))