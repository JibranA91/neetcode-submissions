class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] < 0 or nums[i] > n:
                i += 1
                continue
            
            loc = nums[i] - 1

            if nums[i] != nums[loc]:
                nums[i], nums[loc] = nums[loc], nums[i]
            else:
                i += 1

        print(nums)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
