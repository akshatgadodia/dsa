class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                length = 1

                while current + 1 in nums_set:
                    current += 1
                    length += 1

                result = max(result, length)

        return result


        for idx, num in enumerate(nums):
            index[num] = idx
            value = 1 + count_elements(num, previous=True) + count_elements(num, previous=False)
            result = max(value, result)

        return result 