class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for dig in s:
            if dig in pairs:
                if not stack or stack[-1] != pairs[dig]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(dig)
        return not stack