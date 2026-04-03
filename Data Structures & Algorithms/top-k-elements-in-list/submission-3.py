class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_bucket = [[] for i in range(len(nums))]
        count = dict(collections.Counter(nums))

        for n,c in count.items():
            count_bucket[c-1].append(n)
        
        
        return sum([c for c in count_bucket if c][::-1], [])[:k]