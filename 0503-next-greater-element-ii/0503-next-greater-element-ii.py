class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []                              # holds indices
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                index = stack.pop()             # pop from STACK, not nums
                answer[index] = nums[i % n]     # write the VALUE
            if i < n:                            # only push during the first lap
                stack.append(i)
        return answer


         