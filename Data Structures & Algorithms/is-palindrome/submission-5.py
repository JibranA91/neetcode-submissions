class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = "".join([c.lower() for c in s if c.isalnum()])
        L,R= 0,len(p)-1
        while L < R:
            if p[L] != p[R]:
                return False
            L += 1
            R -= 1
        return True if not p else p[L] == p[R]