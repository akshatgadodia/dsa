class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        result = [0] * n

        carry = 0
        for i in range(n-1, -1, -1):
            value = carry + num[i]

            if i == n - 1:
                value += k
            
            carry = value // 10
            result[i] = value % 10
        
        while carry > 0:
            result.insert(0, carry % 10)
            carry = carry // 10

        return result
        