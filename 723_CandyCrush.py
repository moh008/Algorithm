class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])
        def find_and_mark():
            completed = True
            for r in range(1, ROWS-1):
                for c in range(COLS):
                    if abs(board[r-1][c]) == abs(board[r][c]) == abs(board[r+1][c]) and board[r][c] != 0:
                        board[r-1][c] = -abs(board[r-1][c])
                        board[r][c] = -abs(board[r][c])
                        board[r+1][c] = -abs(board[r+1][c])
                        completed = False
            for r in range(ROWS):
                for c in range(1, COLS - 1):
                    if abs(board[r][c-1]) == abs(board[r][c]) == abs(board[r][c+1]) and board[r][c] != 0:
                        board[r][c-1] = -abs(board[r][c-1])
                        board[r][c] = -abs(board[r][c])
                        board[r][c+1] = -abs(board[r][c+1])
                        completed = False
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] < 0:
                        board[r][c] = 0
            return completed
        
        def drop():     #0의 개수만큼 row를 shift하는 로직
            for c in range(COLS):
                lowest_zero = -1
                for r in range(ROWS-1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1

        while not find_and_mark():
            drop()
        return board