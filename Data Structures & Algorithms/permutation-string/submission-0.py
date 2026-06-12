class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        l = 0
        counts_s1 = [0]*26
        counts_s2 = [0]*26

        for c in s1:
            counts_s1[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            counts_s2[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) > len(s1):
                counts_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if counts_s1 == counts_s2:
                return True
        return False
            






        