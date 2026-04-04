class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ind = {}

        for i, n in enumerate(nums):
            if n in ind and i - ind[n] <= k:
                return True
            ind[n]=i
        
        return False

