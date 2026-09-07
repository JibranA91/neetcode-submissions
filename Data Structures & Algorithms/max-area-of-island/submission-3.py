class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_size=0


        def bfs(r,c):
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                for dr,dc in dirs:                    
                    r,c=row+dr,col+dc
                    if (
                        r in range(ROWS) and c in range(COLS) and
                        (r,c) not in visited and 
                        grid[r][c] == 1
                    ):
                        visited.add((r,c))
                        q.append((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visited:
                    total_visited = len(visited)
                    bfs(r,c)
                    max_size = max(max_size, len(visited) - total_visited)
        
        return max_size