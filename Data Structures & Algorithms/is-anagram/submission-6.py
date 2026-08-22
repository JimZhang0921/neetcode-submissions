class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dic_s = {}
            for i in s:
                dic_s[i] = dic_s.get(i, 0)+1
            for i in range(len(t)):
                if dic_s.get(t[i], 0) <= 0:
                    return False
                else:
                    dic_s[t[i]] -= 1
            return True
