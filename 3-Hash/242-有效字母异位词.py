class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        用defauldict或者collection可以直接比较秒了
        用数组,字母的ascii码或者相对于'a'的ascii码差值作为下标,元素就是字母频数,只使用1个record数组记录s字符串频数, 到了t的时候反向统计频数, 
        也就是说record遍历s字符串遇到一个字母频数+1, 遍历t遇到一个字母频数-1
        """
        s_dict={}
        t_dict={}
        
        for i in s:
            if i in s_dict:
                s_dict[i]+=1
            else:
                s_dict[i]=1
        
        for j in  t:
            if j in t_dict:
                t_dict[j]+=1
            else:
                s_dict[i]=1
        
        for w in s_dict:
            if w not in t_dict or t_dict[w]!=s_dict[w]:
                return False
        
                
        
        return True