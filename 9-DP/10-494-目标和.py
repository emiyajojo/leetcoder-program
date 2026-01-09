from typing import *
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_=sum(nums)
        if (sum_+target)%2!=0 or abs(target)>sum_:
            return 0
        bag_size=(sum_+target)//2
        dp=[0]*(bag_size+1)
        dp[0]=1
        for num in nums:
            for wei in range(bag_size,num-1,-1):
                dp[wei]+=dp[wei-num]
        
        return dp[-1]