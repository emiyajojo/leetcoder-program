from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pro_set={
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        res=[]
        def dfs(di_ind,st,path:list):
            """
            思路: 深度,也就是每次递归传的参数di_ind是当前深度
            宽度,就是从哪个集合体(这个集合不是python集合而是广义上的集合)取值
            """
            if len(path)==len(digits):
                res.append("".join(path))
                return
            button_str=pro_set[int(digits[di_ind])]
            for i in range(st,len(button_str)):
                path.append(button_str[i])
                dfs(di_ind+1,0,path)
                path.pop()
        
        dfs(0,0,[])
        return res

sol=Solution()
print(sol.letterCombinations("23"))