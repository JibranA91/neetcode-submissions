class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {c:0 for c in s}
        L=0
        longest = 0
        for R in range(len(s)):
            freq[s[R]] += 1
            maxf = max(freq.values())
        
            while ((R - L + 1) - maxf) > k:
                freq[s[L]] -= 1
                L += 1
            
            longest = max(longest, (R - L + 1))
        
        return longest