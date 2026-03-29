class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_dict = {}
        for i,n in enumerate(nums):
            ind_dict[n] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ind_dict and ind_dict[diff] > i:
                return [i, ind_dict[diff]]

