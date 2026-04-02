class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (
                r not in range(ROWS) or 
                c not in range(COLS) or 
                grid[r][c] == 0 or 
                (r,c) in visited
                ):
                return 0
            
            visited.add((r,c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        if grid:
            for r in range(ROWS):
                for c in range(COLS):
                    maxSize = max(dfs(r,c), maxSize)            

        return maxSize