class Solution:
    """
    思路:used的去重和递增子序列又不一样,这里used需要在深度的维度上去重
    同时,由于排列的每个元素的长度相同,也就是每个"组合"的元素多少相等,因此排列不需要开始下标,因为每次都要遍历整个数组
    """
    def permute(self, nums):
        res=[]
        path=[]
        used=[False]*len(nums)
        def dfs(path:list,used:list):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                dfs(path,used)
                path.pop()
                used[i]=False
        
        dfs(path,used)
        return res

nums=[1,2,3]
sol=Solution()
print(sol.permute(nums))