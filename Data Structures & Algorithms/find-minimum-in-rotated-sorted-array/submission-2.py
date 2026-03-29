class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        def bin_search(nums, L=0, R=None):
            if R is None:
                R = len(nums)-1

            if R-L <= 1:
                print(L,R, nums[L:R+1])
                if nums[L] < nums[R]:
                    return nums[L]
                return nums[R]

            M = L+(R-L)//2

            print(L, M, R, nums[L:R+1])

            if nums[L] < nums[M] and nums[M] > nums[R]:
                # right
                return bin_search(nums, M, R)
            elif nums[M] < nums[R]:
                # left
                return bin_search(nums, L, M)
        
        return bin_search(nums)


# 1,2,3,4,5,6,7,8 ->> L < M < R ->> go left
# 3,4,5,6,7,8,1,2 ->> L < M > R ->> go right
# 7,8,1,2,3,4,5,6 ->> L > M < R ->> go left