class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0:1}

        res = pref_sum = 0
        for n in nums:
            pref_sum += n
            diff = pref_sum - k
            res += sum_dict.get(diff,0)
            sum_dict[pref_sum] = 1 + sum_dict.get(pref_sum,0)
        
        return res
