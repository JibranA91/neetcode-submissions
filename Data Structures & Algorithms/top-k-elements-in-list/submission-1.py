class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = collections.defaultdict(list)
        for n,c in collections.Counter(nums).items():
            count_dict[c].append(n)
        
        print(count_dict)
        res = []
        while k > 0:
            for v in count_dict.pop(max(count_dict)):
                k -= 1
                res.append(v)
                if k == 0:
                    break
        
        return res

        