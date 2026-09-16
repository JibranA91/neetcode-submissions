class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()


        def bfs(r,c):
            q = collections.deque([(r,c)])
            visited.add((r,c))

            while q:
                r,c = q.popleft()
                
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and 
                    nc in range(cols) and 
                    (nr,nc) not in visited and 
                    grid[nr][nc]=="1"):
                        visited.add((nr,nc))
                        q.append((nr,nc))
        
        lands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    lands += 1
        
        return lands