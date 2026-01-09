class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        square_nums=[i**2 for i in range(n+1) if i**2<=n and i**2>0]
        for num in square_nums:
            for j in range(num,n+1):
                dp[j]=min(dp[j],dp[j-num]+1)
        
        return dp[-1]
        
