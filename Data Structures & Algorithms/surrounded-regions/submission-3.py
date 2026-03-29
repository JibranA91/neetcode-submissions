class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        o = set()

        for r in [0,ROWS-1]:
            for c in range(COLS):
                print(r,c)
                if board[r][c] == 'O':
                    o.add((r,c))
        
        for c in [0,COLS-1]:
            for r in range(ROWS):
                print(r,c)
                if board[r][c] == 'O':
                    o.add((r,c))
        
        visited = set()
        def dfs(r,c):
            if (
                (r,c) in visited or 
                r == ROWS or c==COLS or min(r,c) < 0 or
                board[r][c] == 'X'
                ):
                return            

            visited.add((r,c))
            if board[r][c] == 'O':
                board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
        
        
        for r,c in o:
            dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
                






