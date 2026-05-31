from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parentheses = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in parentheses.keys():
                stack.append(c)
            elif c in parentheses.values():
                if stack and c == parentheses[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


