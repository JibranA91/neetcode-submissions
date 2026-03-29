class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        def twoSum(num_list, target):
            ind_dict = {n:i for i,n in enumerate(num_list)}

            covered = set()
            c_list = []
            for i, n in enumerate(num_list):
                if n in covered: continue
                covered.add(n)
                diff = target - n
                if ind_dict.get(diff,-1) > i:
                    c_list.append([n, diff])
            
            return c_list

        nums.sort()
        covered = set()
        f_res = []
        for i,n in enumerate(nums):
            if n in covered: continue
            covered.add(n)

            diff = 0 - n
            res = twoSum(nums[i+1:], diff)
            if len(res) > 0:
                f_res += [[n]+l for l in res]
            
        
        return f_res
        

