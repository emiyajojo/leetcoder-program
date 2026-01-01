class Solution:
    def fib(self, n: int) -> int:
        """
        1. dp[i]:即斐波那契数,i就是第几个斐波那契
        2. dp[i]=dp[i-1]+dp[i-2]
        3. 初始化:边界条件判断,若n==0, 返回0, 0<n<=2, 返回1
        dp=[0]*n
        4. 递归顺序: 直接递归range(2,n)
        5. 推导
        """
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]
    
sol=Solution()
print(sol.fib(4))