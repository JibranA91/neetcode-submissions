class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ind = {}
        for j,n in enumerate(nums):
            if n in ind and abs(ind[n] - j) <= k:
                return True
            ind[n] = j
        
        return False


