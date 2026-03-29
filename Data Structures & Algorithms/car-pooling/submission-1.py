class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        
        point = {}
        for p in trips:
            point[p[1]] = point.get(p[1],0) - p[0]
            point[p[2]] = point.get(p[2],0) + p[0]

        point = [(k,v) for k,v in point.items()]
        point.sort()
        
        cap = capacity
        for p,c in point:                   
            cap += c
            
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