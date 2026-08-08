import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for row in range(len(matrix)):
            heapq.heappush(heap, (matrix[row][0], row, 0))

        for _ in range(k):
            value, row, col = heapq.heappop(heap)

            if col + 1 < len(matrix[row]):
                heapq.heappush(
                    heap,
                    (matrix[row][col + 1], row, col + 1)
                )

        return value