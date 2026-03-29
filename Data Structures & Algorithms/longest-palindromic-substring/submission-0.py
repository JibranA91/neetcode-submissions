class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resL = 0
        def check_pal(s,l,r):
            res = ""
            resL = 0
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if r-l+1 > resL:
                    resL = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            return res, resL

        for i in range(len(s)):
            l = r = i
            f_res, f_resL = check_pal(s, l, r)
            if f_resL > resL:
                res, resL = f_res, f_resL

            l, r = i, i+1
            f_res, f_resL = check_pal(s, l, r)
            if f_resL > resL:
                res, resL = f_res, f_resL
        
        return res
