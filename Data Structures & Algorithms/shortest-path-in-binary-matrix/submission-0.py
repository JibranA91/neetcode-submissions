class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] or grid[ROWS-1][COLS-1]:
            return -1

        dirs = [
            (0,1),(1,0),(1,1),
            (-1,0),(0,-1),(-1,-1),
            (1,-1),(-1,1)
            ]

        q = collections.deque()
        q.append((0,0,1))
        visited = set()

        while q:
            r,c,l = q.popleft()
            visited.add((r,c))
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if (
                    nr<ROWS and nc<COLS and 
                    min(nr,nc) >= 0 and 
                    (nr,nc) not in visited and 
                    grid[nr][nc]==0 ):
                    if (nr,nc) == (ROWS-1,COLS-1):
                        return l+1
                    q.append((nr,nc,l+1))
                
        return -1