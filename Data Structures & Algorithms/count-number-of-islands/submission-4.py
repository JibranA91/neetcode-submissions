class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r,c):
            if (
                r in range(ROWS) and c in range(COLS)
                and (r,c) not in visited and grid[r][c]=="1"
                ):
                visited.add((r,c))
                for dr,dc in directions:
                    dfs(r+dr, c+dc)
            else:
                return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        

        return islands
