class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2,3,4,5,6] L < M < R
        # [3,4,5,6,1,2] L < M > R

        # [5,6,1,2,3,4] L > M < R
        

        L = 0
        R = len(nums) - 1

        while L <= R:
            M = (L+R)//2
            if nums[M] == target:
                return M
            
            if nums[L] <= nums[M]:
                if target > nums[M] or target < nums[L]:
                    L = M + 1
                else:
                    R = M - 1
            
            else:
                if target > nums[R] or target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1      

        return -1
