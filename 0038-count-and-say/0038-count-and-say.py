class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = self.countAndSay(n - 1)

        rle = ""
        count = 1

        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                count += 1
            else:
                rle += str(count) + result[i - 1]
                count = 1

        rle += str(count) + result[-1]

        return rle