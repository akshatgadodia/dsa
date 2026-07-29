class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}          # char -> last index we saw it
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # if char is in the window (seen at or after left), jump left past it
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length