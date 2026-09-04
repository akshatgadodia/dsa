class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # if len(nums) == 1:
            # return 0

        max_value = nums[0]
        for idx, val in enumerate(nums):
            if val > max_value:
                max_value = val
            
            min_value = min(nums[idx:])
            
            if max_value - min_value <= k:
                return idx
        
        return -1
            

        