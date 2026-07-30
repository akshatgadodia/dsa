from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        left = 0
        max_freq = 0
        longest = 0

        for right in range(len(s)):
            # Add current character to the window
            freq[s[right]] += 1

            # Update the highest frequency seen in the current window
            max_freq = max(max_freq, freq[s[right]])

            # If more than k replacements are needed,
            # shrink the window from the left
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update the answer
            longest = max(longest, right - left + 1)

        return longest