class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L=R=0
        max_len = 0
        while L <=R and R < len(s):
            while s[R] in window and L < R:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            max_len = max(max_len, len(window))
            R += 1
        
        return max_len


