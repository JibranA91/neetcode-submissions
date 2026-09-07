class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = set()
        rotten = set()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.add((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        

        def add_cell(r,c):
            if (
                r in range(ROWS) and c in range(COLS) and 
                grid[r][c]==1 and (r,c) not in visited):
                fresh.remove((r,c))
                visited.add((r,c))
                q.append((r,c))

        if not fresh and not rotten:
            return 0

        q = collections.deque(rotten)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        minutes=-1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                _=[add_cell(r+dr,c+dc) for dr, dc in dirs]
            minutes += 1
        
        return -1 if fresh else minutes



            