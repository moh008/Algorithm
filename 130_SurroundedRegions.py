class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        #a recursive DFS to traverse all direction r +- 1, c +- 1
        def capture(r, c):  #when the traversing is outta range, do nothing
            if(r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        #unsurrounded O the cell is in boarder
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1] and board[r][c] == "O":
                    capture(r, c)
        #surrounded O. the cell is surrounded by X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        #UnCapture unsurrounded "O". Make T cells back to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"