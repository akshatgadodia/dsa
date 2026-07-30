from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)          # Required frequency of each character
        window = defaultdict(int)  # Current window frequencies

        required = len(need)        # Number of unique chars we need
        formed = 0                  # Number of chars currently satisfying required freq

        left = 0
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            # Character requirement just got satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink while the window is valid
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                # Window became invalid
                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ):
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]