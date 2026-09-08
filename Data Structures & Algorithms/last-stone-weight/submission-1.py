class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        maxHeap = [s*-1 for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -1*heapq.heappop(maxHeap)
            y = -1*heapq.heappop(maxHeap)
            if x == y: continue
            elif x < y:
                heapq.heappush(maxHeap, -1*(y-x))
            elif y < x:
                heapq.heappush(maxHeap, -1*(x-y))

        
        return -1*heapq.heappop(maxHeap) if maxHeap else 0