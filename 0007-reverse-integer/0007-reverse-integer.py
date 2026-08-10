class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)

        n = 0

        while x > 0:
            digit = x % 10
            n = (n * 10) + digit
            x = x // 10
        
        if negative:
            n = -n

        if n < -2**31 or n > 2**31 - 1:
            return 0

        return n
        