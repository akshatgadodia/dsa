import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Use Max Heap
        # Add to Heap all elements first
        # while heap:
        #   y = heap.pop()
        #   x = heap.pop()
        #   if y > x: insert y-x in heap
        #   if y but not x then return y

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while heap:
            y = -(heapq.heappop(heap))
            if len(heap) == 0:
                return y
            x = -(heapq.heappop(heap))
            if y > x:
                heapq.heappush(heap, -(y - x))
            
        return -(heap[0]) if len(heap) > 0 else 0