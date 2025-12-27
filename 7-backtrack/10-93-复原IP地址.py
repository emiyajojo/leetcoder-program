# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

#     例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

# 示例 1：

# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]

# 示例 2：

# 输入：s = "0000"
# 输出：["0.0.0.0"]

# 示例 3：

# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

# 提示：

#     1 <= s.length <= 20
#     s 仅由数字组成
from typing import *


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        回忆一下回文串分割思路:
        1. 边界条件判断
        2. for循环:
            这里,是要以当前递归层传入的开始下标为头, 以当前for循环的循环下标为尾进行遍历
            那么深度? 假设当前for循环到了i, 那么就以i为尾取当前的子串进行判断,但是以i+1为头进行向下递归
        
        本题基本一样,但是有个问题就是长度限制: IP地址最长的是4个3位数拼接, 比如255.255.255.255, 12位数字
        若是当前的s长度>12,就可以返回,若是太短<4也可以返回
        还有0开头的数字
        同时要注意combine加入结果集的条件,只有满足了combine有4个元素并且此时已经遍历完整个候选s才将combine加入结果集
        """
        len_s = len(s)
        if len_s < 4 or len_s > 12:
            return []
        res = []

        def dfs(st, combine: list):
            nonlocal len_s
            if st == len(s) and len(combine) == 4:
                res.append(".".join(combine[:]))
                return
            # if len(combine)==4:
            #     return
            for end in range(st, len_s):
                ip_a_s = s[st:end + 1]
                ip_a = int(ip_a_s)
                if (ip_a <= 255 and ip_a
                        >= 0) and not (ip_a_s[0] == '0' and len(ip_a_s)
                                       > 1):  # 要排除0开头的数字串, 当然不能排除0本身
                    combine.append(ip_a_s)
                    dfs(end + 1, combine)
                    combine.pop()

        dfs(0, [])
        return res


sol = Solution()
s = "101023"
res = sol.restoreIpAddresses(s)
for r in res:
    print(r)
