class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(bopen=0, bclose=0):
            if bopen == bclose == n:
                res.append("".join(stack))
                return
            
            if bopen < n:
                stack.append('(')
                backtrack(bopen+1, bclose)
                stack.pop()
            if bclose < bopen:
                stack.append(')')
                backtrack(bopen, bclose+1)
                stack.pop()
            
        
        backtrack()
        return res