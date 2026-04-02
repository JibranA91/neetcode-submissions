class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        treasures = [(r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c]==0]

        def bfs(r,c):
            visited = set()
            q = collections.deque()
            q.append((r,c,0))
            visited.add((r,c))
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]

            while q:
                row, col, d = q.popleft()
                grid[row][col] = min(d, grid[row][col])
                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] not in [0,-1] and (r,c) not in visited:
                        q.append((r,c,d+1))
                        visited.add((r,c))
        
        for tr, tc in treasures:
            bfs(tr, tc)

