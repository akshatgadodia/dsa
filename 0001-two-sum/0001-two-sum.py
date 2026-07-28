class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for idx, val in enumerate(nums):
            required_val = target - val
            if required_val in numbers:
                return [numbers[required_val], idx]
            numbers[val] = idx
        return [0, 0]