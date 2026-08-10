class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in result:
                result[sorted_s].append(s)
            else:
                result[sorted_s] = [s]
        
        return list(result.values())


        