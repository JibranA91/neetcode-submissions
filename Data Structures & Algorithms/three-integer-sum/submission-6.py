class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        for i,n1 in enumerate(nums[:-2]):
            target = 0 - n1
            nums2 = nums[i+1:]
            for j,n2 in enumerate(nums2[:-1]):
                num_set = set(nums2[j+1:])
                if (target - n2) in num_set:
                    res.add(tuple(sorted([n1, n2, target - n2])))
            
        return [list(t) for t in res]
