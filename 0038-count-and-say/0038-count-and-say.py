class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = self.countAndSay(n-1)

        char, count = 0, 0
        rle = ""
        
        for idx in range(len(result)):
            if idx > 0 and result[idx] != result[idx - 1]:
                rle += f"{count}{char}"
                count = 0
            char = result[idx]
            count += 1
        
        rle += f"{count}{char}"
        
        return rle

        