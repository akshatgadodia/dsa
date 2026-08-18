class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = []
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            char = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return "".join(result)
                
            result.append(char)
        
        return "".join(result)