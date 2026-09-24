class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        if not grid: return max_area

        def bfs(r,c,area=1):
            q = collections.deque([(r,c)])
            visited.add((r,c))
            while q:
                r,c = q.popleft()                
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and 
                    nc in range(cols) and 
                    (nr,nc) not in visited and 
                    grid[nr][nc]==1):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            
            return area


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))
        
        return max_area