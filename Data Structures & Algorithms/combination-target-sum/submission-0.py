class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        subsets=[]
        def dfs(i=0, total=0):

            if total == target:
                res.append(subsets.copy())
                return     

            if i >= len(nums) or total > target:
                return
                   
            subsets.append(nums[i])
            dfs(i, total + nums[i])

            subsets.pop()
            dfs(i+1, total)        

        dfs()
        return res