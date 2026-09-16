class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        
        counts = collections.Counter(nums)
        for n,c in counts.items():
            buckets[c-1].append(n)
        
        res = []
        for l in buckets[::-1]:
            res += l
            if len(res) >= k:
                return res[:k]

