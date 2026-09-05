class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        if len(s1) > len(s2):
            return False

        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for i in range(len(s1)):
            s1_map[s1[i]] += 1
            s2_map[s2[i]] += 1

        l=0
        for r in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True
            
            s2_map[s2[r]] += 1
            s2_map[s2[l]] -= 1

            if s2_map[s2[l]] < 1:
                s2_map.pop(s2[l])

            l += 1
        
        return s1_map == s2_map

