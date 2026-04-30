class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in s1:
            cnt1[ord(i) - ord('a')] += 1
        for i in range(len(s2)):
            cnt2[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                cnt2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if cnt1 == cnt2:
                return True
        return False