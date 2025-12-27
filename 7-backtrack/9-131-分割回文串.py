from typing import *
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        这道题又有点不一样,这道题是要候选集的所有元素都算进去,也就是说,是分割而不是单纯地选
        那么就有两个要点:
        1. 不只是要用start, 还要用end, 结合递归和for循环刚好记录当前分割出来的子串
        2. 对于剪枝,只在分割出来的子串满足回文才递归,同时,在for循环之前若是子串起始位置已经末尾,那么就直接返回
        3. 同时要注意,path本质上是指不同的分割方式,因此也是需要记录的
        """
        res=[]
        def dfs(st,path:list):
            if st==len(s):
                res.append(path[:])
                return
            for end in range(st,len(s)):
                sub=s[st:end+1]
                if sub==sub[::-1]:
                    path.append(sub)
                    dfs(end+1,path)
                    path.pop()

        dfs(0,[])
        return res
        