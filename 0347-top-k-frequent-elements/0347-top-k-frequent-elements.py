import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = Counter(nums)
        
        heap = []
        for key, value in elements.items(): 
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for (val, key) in heap:
            result.append(key)
        
        return result


        