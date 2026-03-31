class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []
        subset = []

        def dfs(i=0, total=0):
            if total == target:
                res.append(subset[:])
                return
            if i >= len(nums) or total > target:
                return            

            subset.append(nums[i])
            dfs(i+1, total+nums[i])

            subset.pop()
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i += 1

            dfs(i+1, total)
        
        dfs()
        return res