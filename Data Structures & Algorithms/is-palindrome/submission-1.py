class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = [c.lower() for c in s if c.isalnum()]
        filtered_s == filtered_s[::-1]
        left, right = 0, len(filtered_s)-1
        while left < right:
            if filtered_s[left] != filtered_s[right]:
                return False
            left+=1
            right-=1
        return True
            