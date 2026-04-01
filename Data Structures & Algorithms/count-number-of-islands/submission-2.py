class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        if not grid:
            return islands

        def dfs(r,c):

            if (r not in range(ROWS) or 
            c not in range(COLS) or 
            (r,c) in visited or 
            grid[r][c] == "0"):
                return
            
            visited.add((r,c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        
        return islands