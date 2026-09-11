class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        asum=0
        res = float("Inf")
        for r in range(len(nums)):
            asum += nums[r]            

            while asum >= target:
                res = min(res, r-l+1)
                asum -= nums[l]
                l += 1
        
        return 0 if res == float("Inf") else res
