class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "," + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ""
            while(s[i] != ','):
                num += s[i]
                i += 1
            count = int(num)
            i += 1
            curr = ""
            for j in range(count):
                curr += s[i]
                i += 1
            res.append(curr)
        return res



        
            
