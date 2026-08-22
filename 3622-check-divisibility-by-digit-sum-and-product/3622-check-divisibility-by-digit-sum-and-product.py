import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_sum, n_prod = 0, 1
        original = n

        while n > 0:
            digit = n % 10
            n_sum += digit
            n_prod *= digit

            n //= 10

        return original % (n_sum + n_prod) == 0
        