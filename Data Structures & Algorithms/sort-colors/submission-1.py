class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter

        counts = Counter(nums)

        print(counts)
        j=i=0
        for c in [0,1,2]:
            if c not in counts: continue
            for i in range(counts[c]):
                nums[i+j] = c
            j += i+1

