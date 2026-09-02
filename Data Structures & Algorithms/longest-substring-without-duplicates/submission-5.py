class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        unique = set()
        L=0
        for R in range(len(s)):
            if s[R] not in unique:
                unique.add(s[R])
                max_len = max(max_len, len(unique))
            else:
                while s[L] != s[R]:
                    unique.remove(s[L])
                    L += 1

                unique.add(s[L])
                L += 1
        
        return max_len
