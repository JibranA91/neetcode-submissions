class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l = r = 0
        maxf=0
        count = defaultdict(int)
        maxsize = 0

        while r < len(s):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while ((r-l+1) - maxf) > k:
                count[s[l]] -= 1
                l += 1

            maxsize = max(maxsize, (r-l+1))
            
            r += 1
        
        return maxsize


