class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        val_dic = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c in val_dic: 
                if stack and val_dic[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return not stack