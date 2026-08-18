class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            complete_days = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight <= capacity:
                    current_weight += weight
                else:
                    complete_days += 1
                    current_weight = weight

                    if complete_days > days:
                        return False

            return True

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (high + low) // 2
            if can_ship(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low 