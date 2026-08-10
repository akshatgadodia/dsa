class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def is_palindrome(word):
            return word == word[::-1]

        def backtrack(start):
            # We have partitioned the entire string
            if start == len(s):
                result.append(current[:])
                return

            # Try every possible substring starting at `start`
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if is_palindrome(substring):
                    current.append(substring)

                    backtrack(end)

                    current.pop()

        backtrack(0)

        return result