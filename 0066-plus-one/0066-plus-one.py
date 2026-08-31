class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        carry = 0

        for i in range(n-1, -1, -1):
            num = carry + digits[i]

            if i == n - 1:
                num += 1

            carry = num // 10
            num = num % 10

            digits[i] = num
            if carry == 0:
                break
        
        if carry != 0:
            digits.insert(0, carry)

        return digits

        