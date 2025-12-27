from typing import  *
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(k,n,st,path:list):
            if sum(path)>n:
                return
            if len(path)==k:
                if sum(path)==n:
                    res.append(path[:])
                return
            for i in range(st,9-(k-len(path))+2):
                path.append(i)
                dfs(k,n,i+1,path)
                path.pop()
        
        dfs(k,n,1,[])
        return res
        