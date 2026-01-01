from typing import *
from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        不能同行,不能同列,不能45度和135度(这两条对角线可以通过记录当前行和列的和以及差来记录)
        检查只需要检查前面的,只需要3个集合就可以
        棋盘需要初始化为完整的棋盘,不过是空白的
        检查还需要传入坐标
        结果集添加符合要求的棋盘副本直接使用
        """
        res=[]
        chess_board=[['.']*n for _ in range(n)]
        col_used=set()
        dia1_used=set()
        dia2_used=set()

        def dfs(row):
            if row==n:
                res_c=deepcopy(chess_board)
                for i in range(len(res_c)):
                    res_c[i]="".join(res_c[i])
                res.append(res_c)
                return
            for i in range(n):
                if i not in col_used and row-i not in dia1_used and row+i not in dia2_used :
                    chess_board[row][i]='Q'
                    col_used.add(i)
                    dia1_used.add(row-i)
                    dia2_used.add(row+i)
                    dfs(row+1)
                    chess_board[row][i]='.'
                    col_used.remove(i)
                    dia1_used.remove(row-i)
                    dia2_used.remove(row+i)
        
        dfs(0)
        return res

sol=Solution()
res=sol.solveNQueens(4)
for c in res:
    print('----------------------------')
    for i in c:
        print(i)
            
            
        
                
        
            
        