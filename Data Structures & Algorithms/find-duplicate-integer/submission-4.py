class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            abs_n = abs(n)

            if nums[abs_n-1] < 0:
                return abs_n

            nums[abs_n-1] = abs(nums[abs_n-1])*-1