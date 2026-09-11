class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def children(lock):
            res = []
            for i in range(4):
                digit = int(lock[i])
                up = (digit+1)%10
                down = digit-1 if digit>0 else 9

                res.append(lock[0:i] + str(up) + lock[i+1:])
                res.append(lock[0:i] + str(down) + lock[i+1:])
            return res
        
        q = collections.deque([('0000',0)])
        visited = set(deadends)

        if "0000" in visited:
            return -1

        while q:
            comb, turns = q.popleft()
            
            for child in children(comb):
                if child not in visited:

                    if child == target:
                        return turns + 1

                    visited.add(child)
                    q.append((child, turns + 1))
        
        return -1

