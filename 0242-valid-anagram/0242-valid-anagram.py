from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        characters = defaultdict(int)
        for char in s:
            characters[char] += 1

        for char in t:
            characters[char] -= 1
        
        for char, count in characters.items():
            if count < 0:
                return False
        
        return True

