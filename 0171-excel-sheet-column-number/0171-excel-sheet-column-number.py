class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle)
        for idx, char in enumerate(columnTitle):
            char_idx = ord(char.upper()) - 64

            result += (char_idx) * (26 ** (n - idx - 1))
        
        return result
        