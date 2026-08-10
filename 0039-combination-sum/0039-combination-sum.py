class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        current = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current[:])
                return
 
            for i in range(start, len(candidates)):
                value = candidates[i]

                if value > remaining:
                    break

                current.append(value)
                backtrack(i, remaining - value)
                current.pop()

        backtrack(0, target)

        return result
