class Solution:
    """
    思路:used的去重和递增子序列又不一样,这里used需要在深度的维度上去重
    同时,由于排列的每个元素的长度相同,也就是每个"组合"的元素多少相等,因此排列不需要开始下标,因为每次都要遍历整个数组
    去重逻辑和组合总和II一样
    used[i - 1] == true，说明同一树枝nums[i - 1]使用过
    used[i - 1] == false，说明同一树层nums[i - 1]使用过
    """
    def permute(self, nums):
        nums.sort()
        res=[]
        path=[]
        used=[False]*len(nums)
        def dfs():
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if not used[i-1] and i>0 and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                print(f"{path},{used}")
                used[i]=True
                dfs()
                path.pop()
                used[i]=False
        
        dfs()
        return res

nums=[1,1,2]
sol=Solution()
print(sol.permute(nums))