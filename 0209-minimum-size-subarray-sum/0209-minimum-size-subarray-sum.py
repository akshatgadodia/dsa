class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        result = len(nums)

        i, j = 0, 0
        current_window = 0
        add = True
        while j < len(nums):
            current_window += nums[j] if add else 0

            if current_window >= target:
                result = min(j - i + 1, result)
                current_window -= nums[i]
                add = False
                i += 1
            else:
                j += 1
                add = True
        
        return result
        