from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        
        sums, sums_dict = nums[:], defaultdict(int)

        for idx, num in enumerate(nums[1:]):
            sums[idx + 1] = sums[idx] + num

        sums_dict[0] = 1
        for idx, num in enumerate(sums):
            req = num - k
            if req in sums_dict:
                result += sums_dict[req]
            
            sums_dict[num] += 1
        
        return result
            