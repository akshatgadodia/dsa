class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()

        result = 0
        closest_distance = float('inf')

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == target:
                    return total

                if total > target:
                    k -= 1
                else:
                    j += 1
                
                distance = abs(total-target)
                if distance < closest_distance:
                    closest_distance = distance
                    result = total
        
        return result
                


        