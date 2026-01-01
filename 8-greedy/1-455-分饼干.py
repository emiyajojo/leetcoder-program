from typing import *
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_i=len(s)-1
        g_i=len(g)-1
        cnt=0
        while s_i>=0 and g_i>=0:
            if s[s_i]>=g[g_i]:
                cnt+=1
                s_i-=1
            g_i-=1
        
        return cnt
            
