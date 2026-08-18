class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for r in range(numRows):
            column_array = []
            for c in range(r + 1):
                if c == 0 or c == r:
                   column_array.append(1)
                   continue
                column_array.append(result[r - 1][c - 1] + result[r - 1][c])
            result.append(column_array)
        return result
                 

        