class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r,c,visit,prevh):
            if (
                r not in range(ROWS) or 
                c not in range(COLS) or 
                (r,c) in visit or 
                heights[r][c] < prevh):
                return
            
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            visit.add((r,c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc, visit, heights[r][c])
            
            return


        pa, at = set(), set()
        for c in range(COLS):
            dfs(0,c, pa, heights[0][c])
            dfs(ROWS-1, c, at, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0, pa, heights[r][0])
            dfs(r, COLS-1, at, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pa and (r,c) in at:
                    res.append([r,c])
        
        return res


