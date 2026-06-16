class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums))]
        counts = dict(collections.Counter(nums))

        for n,c in counts.items():
            bucket[c-1].append(n)
        
        res = []
        for l in bucket[::-1]:
            for n in l:
                res.append(n)
                if len(res) ==k:
                    return res