from typing import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    print(f"j:{j}, i:{i}")
                    print(s[j:i])
                    dp[i]=True
                    break

        
        return dp[-1]
