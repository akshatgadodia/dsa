class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start from end
        # while i > 0:
        #     if nums[i] >= nums[i-1]:
        #         swap and [i-1] becomes the pivot

        n = len(nums)
        if n <= 1:
            return nums

        i = n - 1
        pivot = -1
        while i > 0:
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
            
            i -= 1

        if pivot > -1:
            for i in range(n-1, -1, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break

        i = pivot + 1
        j = n - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
