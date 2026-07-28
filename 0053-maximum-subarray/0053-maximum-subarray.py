class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        best_sum = nums[0]

        for i in nums[1:]:
            if current_sum + i >= i:
                current_sum += i
            else:
                current_sum = i

            best_sum = max(best_sum, current_sum)

        return best_sum