class Solution:
    def isValid(self, s: str) -> bool:
        b_dict = {"{":"}", "[":"]", "(":")",}
        stack = []

        for b in s:
            if b in b_dict:
                stack.append(b)
            else:
                if (not stack) or (b_dict[stack.pop()] != b):
                    return False
        
        return stack == []