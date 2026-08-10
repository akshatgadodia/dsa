class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result, current = [], []

        digits_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(i):
            if i == len(digits):
                result.append(''.join(current))
                return

            for value in digits_map[digits[i]]:
                current.append(value)

                backtrack(i + 1)

                current.pop()
        
        backtrack(0)
        
        return result


        