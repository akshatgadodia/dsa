class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                if current[:] not in result:
                    result.append(current[:])
                return 
            
            for index in range(len(nums)):
                if used[index]:
                    continue

                current.append(nums[index])
                used[index] = True

                backtrack()

                current.pop()
                used[index] = False
            
        backtrack()
        
        return result


        