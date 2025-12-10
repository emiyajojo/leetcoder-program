def build_next(pattern: str) -> list[int]:
    """构建前缀表（next数组）"""
    n = len(pattern)
    next_arr = [0] * n
    
    # j: 前缀末尾位置，也是最长相等前后缀的长度
    # i: 后缀末尾位置
    j = 0
    for i in range(1, n):
        # 不匹配时，j 回退
        while j > 0 and pattern[i] != pattern[j]:
            j = next_arr[j - 1]
        
        # 匹配时，j 前进
        if pattern[i] == pattern[j]:
            j += 1
        
        next_arr[i] = j
    
    return next_arr

if __name__=="__main__":
    patt="aabaaf"
    print(build_next(patt))