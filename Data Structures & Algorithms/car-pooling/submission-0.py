class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pick, drop = {}, {}
        start, stop = float('inf'),0
        for p in trips:
            pick[p[1]] = pick.get(p[1],0) + p[0]
            drop[p[2]] = drop.get(p[2],0) + p[0]
            start = min(start, p[1])
            stop = max(stop, p[2])
        
        cap = capacity
        for r in range(start, stop+1):            
            cap -= pick.get(r,0)            
            cap += drop.get(r,0)
            
            print(r, cap)
            if cap < 0 or cap > capacity:
                return False

        return True 


        
            
        

        





"""
cap = 5

1: -2
2: -3
3: 
4: 





"""