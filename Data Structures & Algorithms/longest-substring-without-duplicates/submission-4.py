class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        l,r=0,1
        unique = set()
        unique.add(s[l])
        max_len = 1        

        while r < len(s) and l < r:
            if s[r] not in unique:
                unique.add(s[r])
                max_len = max(len(unique), max_len)
            else:
                while l < r:
                    unique.remove(s[l])
                    if s[l] == s[r]:                        
                        unique.add(s[l])
                        l += 1
                        break
                    l += 1
            r += 1
        
        return max_len