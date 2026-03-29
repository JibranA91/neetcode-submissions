class Solution:
    def findMin(self, nums: List[int]) -> int:

        L, R = 0, len(nums)-1
        res = None
        while L <= R:
            M = (R+L)//2
            res = nums[M] if res is None else min(res, nums[M])

            if nums[M] <= nums[R]:
                R = M -1
            else:
                L = M + 1
        
        return res