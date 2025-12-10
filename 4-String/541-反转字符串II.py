from typing import *
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s):
            l,r=0,len(s)-1
            while l<r:
                s[l],s[r]=s[r],s[l]
                l+=1
                s-=1
            return s
        
        s=list(s)
        
        for i in range(0,len(s),2*k):
            s[i:i+k]=reverse(s[i:i+k])
        
        return "".join(s)
            