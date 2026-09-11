class Solution:
    def longestPalindrome(self, s: str) -> int:

        res = 0
        count = collections.defaultdict(int)

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2
        
        for c,v in count.items():
            if v % 2 == 1:
                res += 1
                break
        
        return res
