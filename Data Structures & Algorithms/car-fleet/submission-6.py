class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        speed_map = {p:s for p,s in zip(position,speed)}
        position = sorted(position, reverse=True)

        time = [round((target-p)/speed_map[p],5) for p in position]

        print(time)
        fleets = [time[0]]

        for t in time:
            if t > fleets[-1]:
                fleets.append(t)
        
        return len(fleets)

        