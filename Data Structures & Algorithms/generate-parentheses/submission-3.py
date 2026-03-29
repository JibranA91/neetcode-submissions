class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def dfs(bopen, bclose):
            if bopen == bclose == n:
                res.append("".join(stack))
                return
            
            if bopen < n:
                stack.append('(')
                dfs(bopen+1, bclose)
                stack.pop()
            if bclose < bopen:
                stack.append(')')
                dfs(bopen, bclose+1)
                stack.pop()
        
        dfs(0,0)
        return res