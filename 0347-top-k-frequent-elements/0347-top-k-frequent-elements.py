class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for n in nums:
            if n in elements:
                elements[n] += 1
            else:
                elements[n] = 1
        
        top_k = dict(nlargest(k, elements.items(), key=lambda item: item[1]))   
        return list(top_k.keys())  

        