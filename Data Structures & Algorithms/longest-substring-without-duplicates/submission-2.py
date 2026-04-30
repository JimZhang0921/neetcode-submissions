class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = 0
        max_cnt = 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= l:
                l = dic[s[i]] + 1
            dic[s[i]] = i
            max_cnt = max(max_cnt, i - l + 1)
        return max_cnt