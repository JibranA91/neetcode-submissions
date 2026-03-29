class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(opened=0, closed=0):
            if opened == closed == n:
                res.append("".join(stack))
                return
            
            if opened < n:
                stack.append('(')
                dfs(opened+1, closed)
                stack.pop()
            if closed < opened:
                stack.append(')')
                dfs(opened, closed+1)
                stack.pop()
            
            return

        dfs()
        return res