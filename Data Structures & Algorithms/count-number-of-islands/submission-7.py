class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()

        if not grid: return 0

        def bfs(r,c):
            visited.add((r,c))
            q = collections.deque([(r,c)])

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nc in range(COLS) and nr in range(ROWS) and (nr,nc) not in visited and grid[nr][nc]=='1':
                        q.append((nr,nc))
                        visited.add((nr,nc))


        lands=0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=='1':
                    bfs(r,c)
                    lands += 1
        
        return lands
