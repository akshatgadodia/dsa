class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numbers, result = set(), set()
        for num in nums1:
            numbers.add(num)

        for num in nums2:
            if num in numbers:
                result.add(num)
        
        return list(result)
