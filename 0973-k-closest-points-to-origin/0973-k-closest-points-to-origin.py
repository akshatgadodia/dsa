import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for [x, y] in points:
            distance = (x ** 2) + (y ** 2)
            distance = math.sqrt(distance)
            print(x, y, distance)

            heapq.heappush(heap, (-distance, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            _, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result
        