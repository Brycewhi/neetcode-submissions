class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = max_len = 0
        window = set()
        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
            else:
                while s[r] in window: 
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
            max_len = max(max_len, len(window))
        return max_len


            