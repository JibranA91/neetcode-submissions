class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):            
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            size = 1

            while q:
                row, col = q.popleft() 
                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if (
                        r in range(ROWS) and 
                        c in range(COLS) and 
                        grid[r][c]==1 and 
                        (r,c) not in visited
                        ):
                        q.append((r,c))
                        visited.add((r,c))
                        size += 1
                        
            return size

        if grid:
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c]==1 and (r,c) not in visited:
                        maxSize = max(maxSize, bfs(r,c))

        return maxSize

