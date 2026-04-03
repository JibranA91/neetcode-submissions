class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        if not operations:
            return 0

        stack = []
        for o in operations:
            if o not in ['+','D','C']:
                stack.append(int(o))
            elif o=='+':
                stack.append(stack[-1] + stack[-2])
            elif o=='D':
                stack.append(stack[-1]*2)
            else:
                _=stack.pop()
        
        return sum(stack)