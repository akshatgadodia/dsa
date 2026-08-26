class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = [0] * 100
        result = 0

        for pair in dominoes:
            number = (
                pair[0] * 10 + pair[1]
            ) if pair[0] >= pair[1] else (
                pair[1] * 10 + pair[0]
            )
            pairs[number] += 1

        for count in pairs:
            result += count * (count - 1) // 2

        return result
        