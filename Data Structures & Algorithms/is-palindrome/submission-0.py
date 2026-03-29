class Solution:
    def isPalindrome(self, s: str) -> bool:

        lower_s = "".join([c.lower() for c in s if c.isalnum()])        
        return lower_s == lower_s[::-1]