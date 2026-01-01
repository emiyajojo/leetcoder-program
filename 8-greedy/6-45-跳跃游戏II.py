from typing import *
class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        cur_cover=0
        size=len(nums)
        next_cover=0
        for i in range(size-1):
            next_cover=max(next_cover,i+nums[i])
            if cur_cover==i:
                res+=1
                cur_cover=next_cover
        
        return res
                