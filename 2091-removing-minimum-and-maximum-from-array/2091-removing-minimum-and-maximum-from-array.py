class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_ele_idx, max_ele_index = 0, 0

        for idx in range(1, n):
            value = nums[idx]

            if value < nums[min_ele_idx]:
                min_ele_idx = idx
            if value > nums[max_ele_index]:
                max_ele_index = idx
            
        remove_from_left = max(min_ele_idx, max_ele_index) + 1
        remove_from_right = n - min(min_ele_idx, max_ele_index)

        remmove_first_from_left = min(min_ele_idx, max_ele_index) + 1
        remove_last_from_right = n - max(min_ele_idx, max_ele_index)
        remove_from_both_ends = remmove_first_from_left + remove_last_from_right

        return min(remove_from_left, remove_from_right, remove_from_both_ends)
        