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