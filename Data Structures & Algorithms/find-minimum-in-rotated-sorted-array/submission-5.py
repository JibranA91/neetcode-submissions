class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = 1001

        while l <= r:
            m = (l + r)//2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1 # [3,4,5,6,1,2]
            else:
                r = m - 1 # [6,1,2,3,4,5]
            
        return res

