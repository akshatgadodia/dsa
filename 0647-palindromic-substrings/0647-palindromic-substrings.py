class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left, right):
            nonlocal count

            while(
                left >= 0
                and right < n
                and s[left] == s[right]
            ):
                left -= 1
                right += 1
                count += 1
        
        for i in range(n):
            expand(i, i)
            expand(i, i+1)
        
        return count
        