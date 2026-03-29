import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)
        n = len(nums)

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(n-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]
        
        
        
        return list(np.array(pre)*np.array(post))


        

# [1,2,4,6]
# pre = [1,1,2,8]
# post = [48,24,6,1]
# res = [48,24,12,8]
