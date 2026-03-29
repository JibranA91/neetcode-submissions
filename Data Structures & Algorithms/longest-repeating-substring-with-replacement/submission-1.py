class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_d = {}
        max_char = 0
        max_len=-1
        L = 0

        for R in range(len(s)):
            window_len = R-L+1

            count_d[s[R]] = count_d.get(s[R],0) + 1            
            rep_req = window_len - max(count_d.values())

            print(L, R, window_len, count_d, rep_req)
            while rep_req > k:
                count_d[s[L]] -= 1
                L += 1
                window_len = R-L+1
                rep_req = window_len - max(count_d.values())

            max_len = max(max_len, window_len)
        
        return max_len
