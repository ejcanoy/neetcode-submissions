class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if (stack[-1] == '[' and ch != ']')  or (stack[-1] == '(' and ch != ')') or (stack[-1] == '{' and ch != '}'):
                    return False
                stack.pop()
        return len(stack) == 0
