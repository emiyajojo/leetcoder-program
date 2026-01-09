from typing import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        本题讲究一个百无禁忌, 结果集要多添加组合
        """
        res=[]
        def dfs(st,combine:list):
            if st==len(nums):

                return
            for i in range(st,len(nums)):
                
                combine.append(nums[i])
                res.append(combine[:])
                dfs(i+1,combine)
                combine.pop()
        
        res.append([])
        dfs(0,[])
        return res

sol=Solution()
res=sol.subsets([1,2,3])
for r in res:
    print(r)