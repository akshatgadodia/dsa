class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []
        used = [False] * len(nums)
        
        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return 
            
            used_at_level = set()

            for index in range(len(nums)):
                if used[index]:
                    continue

                if nums[index] in used_at_level:
                    continue
                used_at_level.add(nums[index])
                

                current.append(nums[index])
                used[index] = True

                backtrack()

                current.pop()
                used[index] = False
            
        backtrack()
        
        return result


        