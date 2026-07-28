class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = nums
        for idx, num in enumerate(nums[1:]):
            result[idx + 1] = result[idx] + num
        
        n = len(nums)

        for idx in range(n):
            sum_left = 0 if idx == 0 else result[idx - 1]
            sum_right = 0 if idx == n-1 else result[n - 1] - result[idx] 

            if sum_left == sum_right:
                return idx
        
        return -1
            
        