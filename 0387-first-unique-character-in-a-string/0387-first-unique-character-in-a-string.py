from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1

        for idx, char in enumerate(s):
            if counts[char] == 1:
                return  idx
        
        return -1

        