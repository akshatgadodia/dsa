class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = pos = n - 1


        result = [0] * n

        while left <= right:
            num1 = nums[left] ** 2
            num2 = nums[right] ** 2

            if num1 > num2:
                result[pos] = num1
                left += 1
            else:
                result[pos] = num2
                right -= 1
            pos -= 1
        
        return result
