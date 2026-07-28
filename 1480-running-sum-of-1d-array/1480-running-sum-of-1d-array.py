class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = nums

        for idx, num in enumerate(nums[1:]):
            result[idx + 1] = result[idx] + num
        
        return result

        