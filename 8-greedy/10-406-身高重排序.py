from typing import *
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        思路和分糖果相似,两个维度,先处理一个维度再处理另一个
        这里,如果先按照前面有多少个不矮于本元素来排的话,按照people[i][1]的定义是按照正序,那么排完之后两个维度都不对
        优先先按照身高逆序排再排people[i][1],那么起码可以确定,前面的节点都比本节点高
        然后,再直接用insert插入就行,排序的时候,把两个维度都插入进去,并且不要用reverse=True, 因为reverse=True会把两个维度都反转,可是这里身高为逆序,people[i][1]为正序,需要改成另一种形式
        """
        # people.sort(key=lambda x:x[0],reverse=True) ❌
        people.sort(key=lambda x:(-x[0],x[1]))
        res=[]
        for p in people:
            res.insert(p[1],p)
    
        return res
            