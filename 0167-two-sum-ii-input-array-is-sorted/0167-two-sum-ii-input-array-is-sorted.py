class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Normal Two Sum Solution
        # number_positions = {}
        
        # for idx, number in enumerate(numbers):
        #     required_target = target - number
        #     if required_target in number_positions:
        #         return [number_positions[required_target] + 1, idx + 1]
            
        #     number_positions[number] = idx

        start, end = 0, len(numbers) - 1
        while True: 
            start_number = numbers[start]
            end_number = numbers[end]

            numbers_sum = start_number + end_number

            if numbers_sum == target:
                return [start + 1, end + 1]
            elif numbers_sum > target:
                end -= 1
            else:
                start += 1

        

        