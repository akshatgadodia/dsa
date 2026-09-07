class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ls = len(s)

        g.sort()
        s.sort()

        j = 0
        result = 0

        for i in range(len(g)):
            while j < ls and s[j] < g[i]:
                j += 1
            
            if j == ls:
                break
            
            result += 1
            j += 1
        
        return result

        