from typing import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        思路:贪心遍历,一路积累剩余的油,当剩余油小于0就把下一个加油站当成七点,同时把剩余油重置为0
        最后若是全部剩余油(gas-cost)总和小于0,返回-1
        """
        cur_gas=0
        total_gas=0
        size=len(gas)
        res=0
        for i in range(size):
            diff=gas[i]-cost[i]
            cur_gas+=diff
            total_gas+=diff
            if cur_gas<0:
                cur_gas=0
                res=i+1
        return res if res<size else -1
        
        
        
        