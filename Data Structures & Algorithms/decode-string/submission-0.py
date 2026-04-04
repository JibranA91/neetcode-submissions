class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                num, char = "", ""
                while stack:
                    e = stack.pop()
                    if e == "[":
                        break
                    else:
                        char = e + char
                
                while stack and stack[-1].isnumeric():
                    e = stack.pop()
                    num = e + num
                stack.append(char*int(num))
                             
            else:
                stack.append(c)
        
        return "".join(stack)
