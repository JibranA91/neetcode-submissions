from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d_list = defaultdict(list)
        for s in strs:
            tup_s = tuple(sorted(s))
            d_list[tup_s].append(s)
        
        return list(dict(d_list).values())