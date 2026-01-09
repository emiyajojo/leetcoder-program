from typing import *
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        思路和打爆气球一样,只不过这里是重叠之后就计数+1并且
        """
        intervals.sort(key=lambda x:x[0])
        res=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[i-1][1]:
                res+=1
                intervals[i][1]=min(intervals[i-1][1],intervals[i][1])
        return res