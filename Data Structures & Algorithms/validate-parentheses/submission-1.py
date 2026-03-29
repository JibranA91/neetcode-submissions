class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cbrackets = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in cbrackets:
                stack.append(c)
            elif stack and stack[-1] == cbrackets[c]:
                _=stack.pop()
            else:
                return False        
        return not stack