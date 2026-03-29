class Solution:
    def majorityElement(self, nums):
        maj_count = len(nums)/2
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
            if counts[n] > maj_count:
                return n