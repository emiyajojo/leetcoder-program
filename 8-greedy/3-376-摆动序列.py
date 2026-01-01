from typing import *
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        3种情况
        其实只需要记得, 记录前一个差的值prediff只需要在prediff和curdiff符号相异(还包括prediff为0的情况,把不等号变成半等号)再更新就行,同时这也是波峰自增的时候
        """
        if len(nums) <= 1:
            return len(nums)  
        prediff,curdiff,res=0,0,1
        for i in range(len(nums)-1):
            curdiff=nums[i+1]-nums[i]
            if (prediff<=0 and curdiff>0) or (prediff>=0 and curdiff<0):
                res+=1
                prediff=curdiff
        return res
        