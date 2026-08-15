class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1

        while left < right:
            current_water_hold = (right - left) * min(height[left], height[right])

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            result = max(result, current_water_hold)
        
        return result
