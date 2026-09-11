class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap: int) -> bool:
            ships, currCap = 1, cap
            for w in weights:
                if w > currCap:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True
        

        while l <= r:
            m = (l+r)//2
            if canShip(m):
                res = min(m, res)
                r = m-1
            else:
                l = m+1
        
        return res

