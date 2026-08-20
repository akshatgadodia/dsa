class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        n = len(num)

        def calculate_result(digit, digit_values):
            if digit <= 3:
                return digit_values[1] * digit
            elif digit == 4:
                return digit_values[1] + digit_values[5]
            elif 5 < digit <= 8:
                return digit_values[5] + (digit_values[1] * (digit - 5))
            elif digit == 9:
                return digit_values[1] + digit_values[10]
            
            return digit_values[digit]

        result = ""            

        values = {
            1: {
                1: 'I',
                5: 'V',
                10: 'X'
            },
            2: {
                1: 'X',
                5: 'L',
                10: 'C'
            },
            3: {
                1: 'C',
                5: 'D',
                10: 'M'
            },
            4: {
                1: 'M',
            }
        }

        for i in range(n - 1, -1, -1):
            digit = int(num[i])

            digit_values = values[n - i]

            digit_result = calculate_result(digit, digit_values)
            # print(digit, digit_values, digit_result)

            result = digit_result + result

        return result

