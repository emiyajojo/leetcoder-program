from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=i=len(nums)-1
        res=[0]*len(nums)
        while l<=r:
            if nums[l]**2<nums[r]**2:
                res[i]=nums[r]**2
                r-=1
            else:
                res[i]=nums[l]**2
                l+=1
            i-=1
        
        return res