from typing import *
class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        思路:两次遍历
        首先注意,无论是哪次遍历,都是在遍历顺序上对比当前元素和前一个元素的大小,比如:
        从左到右遍历:就比较当前元素与左元素大小,从右到左:比较右元素大小
        同时,为了防止第二次遍历的时候由于右元素比较小因此把左元素的值覆盖(比如[....3,4,5,2],从左到右时可能在rating[i]=5这里需要分发4个糖果,如果从右到左,则依然是5个而不是1+1=2个)需要比较pre+1和candy[i],取更大值
        """
        candy=[1]*len(ratings)
        size=len(ratings)
        for i in range(1,size):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1

        for j in range(size-2,-1,-1):
            if ratings[j+1]>ratings[j]:
                candy[j+1]=candy[j]+1

        return sum(candy)

sol=Solution()
ra=[1,3,4,5,2]
print(sol.candy(ra))