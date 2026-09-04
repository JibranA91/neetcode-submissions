class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l = 0
        maxf = 0
        counts = defaultdict(int)
        size = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            maxf = max(maxf, counts[s[r]])

            while (r-l+1) - maxf > k:
                counts[s[l]] -= 1
                maxf = max(maxf, counts[s[l]])
                l += 1
            
            size = max(size, (r-l+1))

        return size
        
        

