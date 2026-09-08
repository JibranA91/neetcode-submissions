class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        chests = [(r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c]==0]
        visited = set(chests)
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        q = collections.deque(chests)
        
        def add_cell(r,c):
            if (r in range(ROWS) and c in range(COLS) 
                and grid[r][c] > 0 and (r,c) not in visited):
                q.append((r,c))
                visited.add((r,c))
            else:
                return

        distance=0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                _=[add_cell(row+dr, col+dc) for dr,dc in dirs]
            distance += 1
            
