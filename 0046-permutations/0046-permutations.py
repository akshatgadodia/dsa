class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        current = []

        def permutation():
            # A complete permutation is formed
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if i in seen:
                    continue

                seen.add(i)
                current.append(nums[i])

                permutation()

                current.pop()
                seen.remove(i)

        permutation()
        return result