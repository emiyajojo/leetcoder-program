"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
示例1
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：

输入：n = 1
输出：[[1]]

 

提示：

    1 <= n <= 20
"""
from typing import List
"""
循环不变量
使用左闭右开规则可以4条边都是1个处理规则
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        stx=sty=0
        times=1
        offset=count=1
        res=[[1]*n for _ in range(n)]
        while times<=n//2:
            for j in range(sty,n-offset):
                res[stx][j]=count
                count+=1
            for i in range(stx,n-offset):
                res[i][n-offset]=count
                count+=1
            
            for j in range(n-offset,sty,-1):
                res[n-offset][j]=count
                count+=1
            for i in range(n-offset,stx,-1):
                res[i][sty]=count
                count+=1
            
            times+=1
            offset+=1
            stx+=1
            sty+=1
        
        if n%2!=0:
            res[n//2][n//2]=count
        return res

if __name__=="__main__":
    sol=Solution()
    nums=sol.generateMatrix(5)
    for num in nums:
        print(num)