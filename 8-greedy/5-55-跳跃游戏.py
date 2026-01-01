from typing import *
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size=len(nums)
        if size==1:
            return True
        cover=0
        for i in range(size):
            if cover>=i:
                cover=max(cover,i+nums[i])
                if cover>=size-1:
                    return True
            else:
                break
        
        return False
        