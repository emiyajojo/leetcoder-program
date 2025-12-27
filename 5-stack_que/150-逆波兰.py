# 给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

# 请你计算该表达式。返回一个表示表达式值的整数。

# 注意：

#     有效的算符为 '+'、'-'、'*' 和 '/' 。
#     每个操作数（运算对象）都可以是一个整数或者另一个表达式。
#     两个整数之间的除法总是 向零截断 。
#     表达式中不含除零运算。
#     输入是一个根据逆波兰表示法表示的算术表达式。
#     答案及所有中间计算结果可以用 32 位 整数表示。

 

# 示例 1：

# 输入：tokens = ["2","1","+","3","*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

# 示例 2：

# 输入：tokens = ["4","13","5","/","+"]
# 输出：6
# 解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

# 示例 3：

# 输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 输出：22
# 解释：该算式转化为常见的中缀算术表达式为：
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# tokens = ["3","11","+","5","-"]

# 1 <= tokens.length <= 104
# tokens[i] 是一个算符（"+"、"-"、"*" 或 "/"），或是在范围 [-200, 200] 内的一个整数
from operator import *
from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        用一个暂时变量存储中间运算值
        若运算值为NOne,那么当进栈了一个运算符,就pop出两个值
        若非空,则pop出1个值,并与中间值运算
        接下来是易错关键：将所谓的中间值塞进栈中！所以并不需要额外的中间值！
        """
        if len(tokens)==1: return tokens[0]
        nums_stack=[]
        def div(num1,num2):
            return int(num1/num2)
        oper_map={'+':add,'-':sub,'*':mul,'/':div}
        
        for item in tokens:
            if item not in oper_map:    nums_stack.append(int(item))
            else:
                num1=nums_stack.pop()
                num2=nums_stack.pop()
                nums_stack.append(oper_map[item](num2,num1))
        
        return nums_stack.pop()    

sol=Solution()
tokens = ["4","13","5","/","+"]
print(sol.evalRPN(tokens))
                
            
        