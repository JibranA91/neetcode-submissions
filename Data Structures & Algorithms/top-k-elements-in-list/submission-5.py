class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        inv_counts = collections.defaultdict(list)
        for n,c in counts.items():
            inv_counts[c].append(n)
        sorted_v = sorted(inv_counts.keys(), reverse=True)

        res = []
        for i in range(k):
            res += inv_counts[sorted_v[i]]
            if len(res) >= k:
                return res[:k]

