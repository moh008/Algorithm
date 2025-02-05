"""
HashSet으로 판단
Row나 Column은 각각 돌면서 있는지 체크하고 hashset에 add했다가 if에서 in rows[r], in cols[c] 하면 그만
3x3 Sqaure는 원래 r, c인덱스의 // 3 값으로 판단 ex) 0 - 2 는 // 3하면 0, 3 - 5까지는 // 3하면 1, 6 - 8까지는 //3하면 2
즉 0,0부터 2,2까지 3x3칸의 9개의 board[r][c] 값들은 square[(0,0)]칸 하나에 다 들어간다고 보면됨
표시하자면 square hashset에 key = [(0, 0)]에 들어간 value는 아래와 같음
square[(0,0): board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1], board[2][2]]
square[(0,1): board[0][3],board[0][4],board[0][5],board[1][3],board[1][4],board[1][5],board[2][3],board[2][4], board[2][5]]
square[(0,2): board[0][6],board[0][7],board[0][8],board[1][6],board[1][7],board[1][8],board[2][6],board[2][7], board[2][8]]
... 이하 반복 square[(2, 2)]까지..
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collection.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True