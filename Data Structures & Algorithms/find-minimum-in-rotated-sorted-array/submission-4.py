class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = nums[L]

        while L <= R:
            M = (L+R)//2

            if nums[L] < nums[R]:
                return min(res, nums[L])

            res = min(res, nums[M])

            if nums[M] < nums[L]:
                R = M-1
            else:
                L = M+1
        
        return res
            