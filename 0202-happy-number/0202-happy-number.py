class Solution:
    def isHappy(self, n: int) -> bool:

        not_happy_numbers = set()
        def sum_of_sqaure_of_digits(num):
            result = 0
            for i in str(num):
                result += int(i) ** 2
            
            if result != 1:
                not_happy_numbers.add(int(num))
            return result
        
        result = n
        while result != 1:
            if result in not_happy_numbers:
                return False
            result = sum_of_sqaure_of_digits(result)

        return True
             
        