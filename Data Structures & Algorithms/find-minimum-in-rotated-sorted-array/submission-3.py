class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n - 1


        while L <= R:
            M = (L+R)//2
            print(nums[L:R])
            if R-L < 1:
                return nums[L]
            
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M


            


# [1,2,3,4,5,6] L
# [6,1,2,3,4,5] L
# [5,6,1,2,3,4] R L > M < R
# [4,5,6,1,2,3] R L < M > R
# [3,4,5,6,1,2] R L < M > R
# [2,3,4,5,6,1] R L < M > R
#  L   M     R
