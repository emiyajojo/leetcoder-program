# 给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。 例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。
# 输入描述
# 输入一个字符串 s,s 仅包含小写字母和数字字符。
# 输出描述
# 打印一个新的字符串，其中每个数字字符都被替换为了number
# 输入示例

# a1b2c3

# 输出示例

# anumberbnumbercnumber

# 提示信息
# 数据范围：
# 1 <= s.length < 10000。
def repalceNum(s):
    count=sum(1 for char in s if char.isdigit())
    len_res=len(s)+count*5
    res=len_res*[""]
    new_ind=len(res)-1
    old_ind=len(s)-1
    while new_ind>=0 and old_ind>=0:
        if s[old_ind].isdigit():
            res[new_ind-5:new_ind]="number"
            new_ind-=6
        else:
            res[new_ind]=s[old_ind]
         
            new_ind-=1
 
        old_ind-=1
 
     
    return "".join(res)
 
if __name__=="__main__":
     
    while True:
        try:
             
                s=input()
                res=repalceNum(s)
                print(res)
        except EOFError:
            break
