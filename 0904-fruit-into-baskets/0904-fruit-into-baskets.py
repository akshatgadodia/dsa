from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        i, j = 0, 0
        
        distinct_elements = defaultdict(int)
        
        while j < len(fruits):
            distinct_elements[fruits[j]] += 1

            while len(distinct_elements) > 2:
                if distinct_elements[fruits[i]] == 1:
                    distinct_elements.pop(fruits[i])
                else:
                    distinct_elements[fruits[i]] -= 1
                i += 1

            result = max(result, j - i + 1)
            j += 1

        return result
            



        