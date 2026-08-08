import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_range = float('inf')
        current_max = float('-inf')
        result = [0 ,0]

        for idx, row in enumerate(nums):
            if row[0] > current_max:
                current_max = row[0]
            
            heapq.heappush(heap, (row[0], idx, 0))
        
        while True:
            min_element, row_idx, col_idx = heapq.heappop(heap)
            if current_max - min_element < max_range:
                max_range = current_max - min_element
                result[0] = min_element
                result[1] = current_max
            
            if len(nums[row_idx]) - 1 == col_idx:
                break
            
            next_element_to_add = nums[row_idx][col_idx + 1]
            if next_element_to_add > current_max:
                current_max = next_element_to_add
            heapq.heappush(heap, (next_element_to_add, row_idx, col_idx + 1))
            
        return result




    