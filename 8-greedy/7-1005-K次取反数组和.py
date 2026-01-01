from typing import *
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x),reverse=True)
        size=len(nums)
        for i in range(size):
            if nums[i]<0 and k>0:
                nums[i]*=-1
                k-=1
        if k%2!=0:
            nums[-1]*=-1

        return sum(nums)

sol=Solution()
nums = [1,2,22,-23,-9,-30,-6,-9,1,8,24,2,21,29,10,-25,18,30,1,9,-8,-11,-22,-23,-17,-12,19,28,19,28]
k = 24
print(sol.largestSumAfterKNegations(nums,k))
                