import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for row in matrix:
            for col in row:
                heapq.heappush(heap, -1 * col)

                if len(heap) > k:
                    heapq.heappop(heap)
        
        return -1 * heap[0]
        