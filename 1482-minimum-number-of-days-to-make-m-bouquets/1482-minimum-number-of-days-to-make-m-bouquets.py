class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        flowers_required = m * k

        if len(bloomDay) < flowers_required:
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)

        def can_make(day):
            bouquets = 0
            consecutive = 0
            for bloom_day in bloomDay:
                if bloom_day <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0

                        if bouquets == m:
                            return True
                else:
                    consecutive = 0
            
            return False

        while low <= high:
            mid = low + (high - low) // 2

            if can_make(mid):
                high = mid - 1
            else:
                low = mid + 1
            
        return low
        