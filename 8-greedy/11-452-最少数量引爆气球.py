from typing import *
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        思路:先排序,然后更新最小边界
        为什么更新?
        只能从竖切的角度去看:假设三个气球可以通过1只箭矢打爆:
        [[1,8],[2,9],[3,10]]
        很明显,这里射8就可以弄爆3个气球,同时8也是这3个重叠气球的最小右边界
        """
        
        points.sort(key=lambda x:x[0])
        res=1
        for i in range(1,len(points)):
            if points[i][0]>points[i-1][1]:
                res+=1
            else:
                points[i][1]=min(points[i][1],points[i-1][1])
        
        return res