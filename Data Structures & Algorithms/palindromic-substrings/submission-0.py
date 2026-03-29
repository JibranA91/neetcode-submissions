class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def check_palindrome(s, L, R):
            count = 0
            while L >=0 and R < len(s):
                if s[L] == s[R]:
                    count += 1
                else:
                    break
                L -= 1
                R += 1

            return count

        count = 0
        for i in range(len(s)):
            count += check_palindrome(s, i, i)
            count += check_palindrome(s, i, i+1)

            
        return count

