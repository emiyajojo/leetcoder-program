from typing import List
class Solution:

    def isHappy(self, n: int) -> bool:
        record_set=set()
        while n not in record_set:
            record_set.add(n)
            sum_=0
            for i in str(n):
                sum_+=i**2
            if sum_==1:
                return True
            n=sum_
        
        return False
    

if __name__=="__main__":
    n=19
    sol=Solution()
    print(sol.isHappy(n))