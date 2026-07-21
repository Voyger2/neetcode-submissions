class Solution:

    def encode(self, strs: List[str]) -> str:
        new = []
        for i in range(len(strs)):
            length = len(strs[i])
            new.append(str(length) + "#" + strs[i])
        new_1 = "".join(new)
        return new_1
    def decode(self, s: str) -> List[str]:
        i = 0
        final = []
        while i < len(s):
            j = i
            while s[j] != "#":
                
                j += 1
            length = int(s[i:j])
            res = s[j+1 : j+1+length]
            final.append(res)
            i = j+1+length
        return final