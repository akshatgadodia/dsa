class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = nums
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            self.sums[idx] = self.sums[idx - 1] + num

    def sumRange(self, left: int, right: int) -> int:
        if right > len(self.sums):
            return -1

        start_value = 0 if left == 0 else self.sums[left -1]
        return self.sums[right] - start_value



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)