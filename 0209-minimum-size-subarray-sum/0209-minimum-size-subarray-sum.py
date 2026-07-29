class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        result = len(nums)

        i, j = 0, 0
        current_window = 0
        
        while j < len(nums):
            current_window += nums[j]

            while current_window >= target:
                result = min(result, j - i + 1)
                current_window -= nums[i]
                i += 1

            j += 1
        
        return result
        