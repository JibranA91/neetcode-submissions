class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                if len(prefix)==1:
                    return ""
                prefix = prefix[0:-1]
        
        return prefix