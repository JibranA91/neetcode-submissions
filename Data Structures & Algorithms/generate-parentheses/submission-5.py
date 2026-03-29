class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(openB=0, closeB=0):
            if openB == closeB == n:
                res.append("".join(stack))
                return
            
            if openB < n:
                stack.append("(")
                dfs(openB+1, closeB)
                stack.pop()
            if closeB < openB:
                stack.append(")")
                dfs(openB, closeB+1)
                stack.pop()
        
        dfs()
        return res