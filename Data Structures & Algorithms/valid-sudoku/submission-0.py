class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for R in range(9):
            for C in range(9):
                if board[R][C] != '.':
                    num = board[R][C]
                    grid_loc = R//3,C//3
                    if (
                        num in rows[R] or 
                        num in columns[C] or
                        num in squares[grid_loc]):
                        return False

                    rows[R].add(num)
                    columns[C].add(num)
                    squares[grid_loc].add(num)
    
        return True



