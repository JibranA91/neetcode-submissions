class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        ind=0
        for a,b in zip(word1,word2):
            res += a+b
            ind += 1
        
        return res + word1[ind:] + word2[ind:]
