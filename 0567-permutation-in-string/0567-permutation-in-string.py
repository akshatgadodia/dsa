from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original_string, window_string = defaultdict(int), defaultdict(int)
        for char in s1:
            original_string[char] += 1

        window_length = len(s1)
        for char in s2[:window_length]:
            window_string[char] += 1

        if dict(original_string) == dict(window_string):
            return True

        print(dict(original_string), dict(window_string))

        for idx, char_to_add in enumerate(s2[window_length:]):
            char_to_remove = s2[idx]

            if window_string[char_to_remove] == 1 or window_string[char_to_remove] == -1:
                window_string.pop(char_to_remove)
            else:
                window_string[char_to_remove] -= 1
            
            window_string[char_to_add] += 1

            print(dict(original_string), dict(window_string))

            if dict(original_string) == dict(window_string):
                return True

        return False

        