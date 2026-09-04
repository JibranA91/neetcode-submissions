class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        unique = set()
        size = 0

        for r in range(len(s)):
            if s[r] not in unique:
                unique.add(s[r])
                size = max(size, len(unique))
            else:
                while s[l] != s[r]:
                    unique.remove(s[l])
                    l += 1
                l += 1
            
        return size


# "zxyyxyz"
# z zx  zxy 