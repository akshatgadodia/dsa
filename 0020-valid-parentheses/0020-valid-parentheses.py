class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['[', '{', '(']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                popped = stack.pop()
                if char == ']' and popped == '[':
                    continue
                elif char == '}' and popped == '{':
                    continue
                elif char == ')' and popped == '(':
                    continue
                else:
                    return False
        return not bool(stack)
        