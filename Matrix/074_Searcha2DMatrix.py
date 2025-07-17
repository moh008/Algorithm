"""
정렬된 matrix에서 2진 탐색법으로 target을 찾아 bool return하는 문제
mid_row, mid_col을 구하는 divmod방식이 포인트. 
left와 right의 중간(mid)에서 중간이라고 불리는 mid_row과 mid_col은 각각 mid에서 컬럼값으로 나눈 몫과 나머지로 결정됨
예를 들어 1 부터 12까지 있는 3 * 4라고 했을때
0  1  2  3  0+11 // 2 = 5 중간값 mid임 mid는 5이지만 5의 row와 col 위치를 결정하려면
4  5  6  7  컬럼숫자로 나눠보면 몫은 그 row가 되고, 나머지는 column값이라는 직관적인 계산이 나옴
8  9 10 11  divmod(5, 4) = 몫: 1, 나머지 1. 즉 5는 1번 (0이 첫번째라고 따졌을시)row와 1번 col에 위치하고있음
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (right + left) // 2
            mid_row, mid_col = divmod(mid, n)
            if matrix[mid_row][mid_col] < target:
                left = mid + 1
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
            else:
                return True
        return False