from typing import *
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        思路: 维持一个滑动窗口, 使用res记录滑动窗口和的最大值, 这个滑动窗口并不需要start,end双指针,只需要在和的值小于0的时候,将窗口和重置为0,即开始指针从当前和为负值的窗口移走
        """
        
        if len(nums)==1:
            return nums[0]
        res=float('-inf')
        sum_=0
        for i in nums:
            sum_+=i
            res=max(sum_,res)
            if sum_<=0:
                sum_=0
        
        return res
            