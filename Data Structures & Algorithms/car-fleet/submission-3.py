class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_map = {p:s for p,s in zip(position, speed)}
        position.sort(reverse=True)
        time = [round((target-p)/speed_map[p],3) for p in position]
        total_fleets = 1

        fleet_leaders = [time[0]]
        for t in time:
            if fleet_leaders[-1] < t:
                fleet_leaders.append(t)           
                

        return len(fleet_leaders)