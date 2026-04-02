class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d_list = collections.defaultdict(list)

        for s in strs:
            d_list[tuple(sorted(s))].append(s)
        
        return list(d_list.values())