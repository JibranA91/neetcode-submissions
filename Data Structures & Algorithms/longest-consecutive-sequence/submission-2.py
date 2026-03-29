class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        num_set = set(nums)
        longest = 1
        for n in nums:
            if n-1 in num_set: 
                continue
            if n+1 in num_set:
                sub_len = 1
                while n+1 in num_set:
                    sub_len +=1
                    num_set.remove(n+1)
                    n = n+1
                longest = max(longest,sub_len)
        
        return longest