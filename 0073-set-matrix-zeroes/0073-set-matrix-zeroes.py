class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows, zero_cols = [], []

        if not matrix:
            return zeros

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        
        if not zero_rows:
            return matrix
        
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        