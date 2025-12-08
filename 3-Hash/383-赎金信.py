class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 类似于有效异位词
        # 区别是，由于有效异位词是需要两个字符串的所有字符频数完全一样，因此使用1个数组先加后减，若是频数完全一样则所有元素都应该为0
        # 本题就不一样，本题要求前一个字符串的所有元素的频数小于等于后一个字符串，因此两个数组，记录两组频数比较大小，或者一个数组先加后减，所有元素必须不小于0
        freq=[0]*26
        for i in magazine:
            freq[ord(i)-ord('a')]+=1
        for i in ransomNote:
            freq[ord(i)-ord('a')]-=1
        for c in freq:
            if c<0:
                return False
        return True