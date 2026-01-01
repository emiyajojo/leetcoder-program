from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size=len(cost)
        dp=[0]*(size)
        dp[0]=dp[1]=0
        for i in range(2,size):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
                
        return min(dp[size-1]+cost[size-1],dp[size-2]+cost[size-2])

sol=Solution()
cost=[1,100,1,1,1,100,1,1,100,1]
res=sol.minCostClimbingStairs(cost)
print(res)