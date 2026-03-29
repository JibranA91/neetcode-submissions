class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        s_points = []
        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set and n+1 in nums_set:
                s_points.append(n)
        
        print(s_points)
        res = 1
        for s in s_points:
            ssize = 0
            while s in nums_set:
                ssize += 1
                s += 1
            res = max(res, ssize)
        
        return res


