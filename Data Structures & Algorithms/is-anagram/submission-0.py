class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)
        for c1, c2 in zip(s,t):
            s_dict[c1] += 1
            t_dict[c2] += 1
        
        return s_dict == t_dict