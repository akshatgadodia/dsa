class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        candidates.sort()
 
        def backtrack(start, remaining):

            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                # Make choice
                current.append(candidates[i])

                # Explore
                backtrack(i + 1, remaining - candidates[i])

                # Undo choice
                current.pop()

        backtrack(0, target)

        return result


            