class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u = set()
        indexes = []
        for i,n in enumerate(nums):
            if n in u:
                indexes.append(i)
            else:
                u.add(n)
        
        for i, index in enumerate(indexes):
            nums.pop(index-i)
        
        return len(nums)