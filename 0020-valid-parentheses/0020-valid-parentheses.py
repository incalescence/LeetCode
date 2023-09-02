class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '{': '}',
            '[': ']',
            '(' : ')',
        }
        if len(s) <= 1:
            return False
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack and char == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True 
        return False       