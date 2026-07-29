class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / len(nums)

        current_window_sum = sum(nums[:k])
        max_avg = current_window_sum / k

        for idx, num in enumerate(nums[k:]):
            current_window_sum += num
            current_window_sum -= nums[idx]

            max_avg = max(max_avg, current_window_sum / k)

        return max_avg