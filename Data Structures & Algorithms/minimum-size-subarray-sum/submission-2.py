class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:    

        if len(nums) == 1 and nums[0] >= target:
            return 1    

        min_res = len(nums)
        c = 0
        L = 0
        total = 0
        for R in range(len(nums)):
            total += nums[R]
            while L <= R and total >= target:                
                min_res = min(min_res, R-L+1)
                total -= nums[L]
                L += 1
                c += 1
        
        return min_res if c else 0

        