class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        
        current_sum = 0
        for i in range(n):
            left_sum[i] = current_sum
            current_sum += nums[i]
        
        current_sum = 0
        for i in range(n-1, -1, -1):
            right_sum[i] = current_sum
            current_sum += nums[i]
        
        result = []
        for i in range(n):
            result.append(
                abs(left_sum[i] - right_sum[i])
            )
        
        return result
            