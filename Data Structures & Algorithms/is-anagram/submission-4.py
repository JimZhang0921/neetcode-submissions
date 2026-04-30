class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic_s = {}
        dic_c = {}
        for i in range(len(s)):
            dic_s[s[i]] = 1 + dic_s.get(s[i], 0)
            dic_c[t[i]] = 1 + dic_c.get(t[i], 0)
        return dic_s==dic_c
        