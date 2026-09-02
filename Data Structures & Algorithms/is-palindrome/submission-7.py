class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=[c.lower() for c in s if c.isalnum() and c!=" "]
        L=0
        R=len(s)-1
        while L <= R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        
        return True