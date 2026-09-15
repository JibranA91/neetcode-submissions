class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = collections.defaultdict(list)

        for s in strs:
            sets["".join(sorted(s))].append(s)
        
        return list(sets.values())