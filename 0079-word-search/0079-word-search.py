class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        visited = set()
        def backtrack(row, col, index):
            nonlocal visited

            if index >= len(word):
                return True
            
            if row < 0 or row == rows or col < 0 or col == cols:
                return False

            if board[row][col] != word[index]:
                return False
            
            if (row, col) in visited:
                return False
            
            index += 1
            visited.add((row, col))

            result = [
                backtrack(row + 1, col, index),
                backtrack(row, col + 1, index),
                backtrack(row - 1, col, index),
                backtrack(row, col - 1, index)
            ]

            index -= 1
            visited.discard((row, col))


            return any(result)
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        
        return False
