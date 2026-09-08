class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        class maxHeap:
            def __init__(self, nums: list[int]):
                import heapq
                self.maxHeap = [s*-1 for s in stones]
                heapq.heapify(self.maxHeap)
            
            def push(self, val: int):
                heapq.heappush(self.maxHeap, -1*val)
            
            def pop(self):
                return -1*heapq.heappop(self.maxHeap)
            
            def __len__(self):
                return len(self.maxHeap)
        
        heap = maxHeap(stones)

        while len(heap) > 1:
            x = heap.pop()
            y = heap.pop()
            if x == y: continue
            elif x < y:
                heap.push(y-x)
            elif y < x:
                heap.push(x-y)

        
        return heap.pop() if len(heap) else 0
