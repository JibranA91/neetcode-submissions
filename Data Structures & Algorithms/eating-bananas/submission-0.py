class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(piles, rate):
            return sum([p//rate + (1 if p%rate>0 else 0) for p in piles])
        
        max_rate = max(piles)
        L, R = 1, max_rate
        while L <= R:
            M = (L+R)//2
            print(M, time_taken(piles, M))
            if time_taken(piles, M) > h:
                L = M+1
            else:
                best_rate = M
                R = M - 1
        return best_rate