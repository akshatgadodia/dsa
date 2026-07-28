class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_string = ''.join(c for c in s if c.isalnum())
        alphanumeric_string = alphanumeric_string.lower()

        return alphanumeric_string == alphanumeric_string[::-1]
        