class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp=[n for n in nums]

        for i,n in enumerate(nums):
            tmp[( i + k ) % len(nums)] = n
        
        for i, n in enumerate(tmp):
            nums[i] = n


