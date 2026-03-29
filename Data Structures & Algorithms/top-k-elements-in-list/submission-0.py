class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_dict = {i:0 for i in nums}
        for n in nums:
            c_dict[n] += 1

        l_dict = collections.defaultdict(list)
        for n,c in c_dict.items():
            l_dict[c].append(n)
        res = []
        while True:
            for n in l_dict.pop(max(l_dict)):
                res.append(n)
                k -= 1
                if k==0:
                    return res