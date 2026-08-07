class Solution:
    def can_finish(self, piles, h, speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2

            if self.can_finish(piles, h, mid):
                right = mid - 1
            else: 
                left = mid + 1
        
        return left