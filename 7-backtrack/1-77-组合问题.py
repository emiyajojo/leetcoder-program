from typing import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.backtrack(n,k,1,[],result)
        return result
        
    def backtrack(self,n,k,startIndex,path:list,result:list):# startIndex 没必要从0开始，因为题目里的全部n个数是从1开始，也没必要用数组存储这n个数
        if len(path)==k:
            result.append(path[:]) # 加上[:]相当于复制了path，而非引用
            return result
        
        for i in range(startIndex, n-(k-len(path))+2): # range()的stop条件带入n=5,k=4看如何剪枝就明白了，+2的话要考虑到剪枝以及range的右括号开区间
            path.append(i)
            self.backtrack(n,k,i+1,path,result)
            path.pop()
