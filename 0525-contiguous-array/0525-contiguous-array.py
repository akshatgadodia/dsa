class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}   # balance -> first index

        balance = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 1:
                balance += 1
            else:
                balance -= 1

            if balance in first_index:
                ans = max(ans, i - first_index[balance])
            else:
                first_index[balance] = i

        return ans