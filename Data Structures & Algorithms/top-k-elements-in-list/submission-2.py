class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        bucket = [[] for i in range(len(nums))]

        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        for a,b in count.items():
            bucket[b-1].append(a)

        rev_bucket = [l for l in bucket if l][::-1]
        res = []
        for l in rev_bucket:
            for n in l:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []
