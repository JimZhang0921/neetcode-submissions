class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str = encode_str + str(len(s))+ "#" + s
        return encode_str
    def decode(self, s: str) -> List[str]:
        strs = []
        i=0
        j = 0
        while i < len(s):
            if s[i] == "#":
                l = int(s[j:i])
                i +=1
                j = i + l
                strs.append(s[i: j])
                i = j
            else:
                i+=1
        return strs