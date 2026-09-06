"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq

        if not intervals:
            return 0
        
        if len(intervals)==1:
            return 1
        
        intervals = sorted(intervals, key=lambda x: x.start)
        rooms = []
        heapq.heappush(rooms, intervals[0].end)

        for i in intervals[1:]:
            if i.start < rooms[0]:
                heapq.heappush(rooms, i.end)
            elif i.start >= rooms[0]:
                _=heapq.heappop(rooms)
                heapq.heappush(rooms, i.end)

        print(rooms)
        return len(rooms)