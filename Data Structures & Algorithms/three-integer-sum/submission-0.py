class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print('\n',nums)
        def twoSum(num_list, target, prev):
            numMap = {n:i for i,n in enumerate(num_list)}

            inner_res = []
            for i,n in enumerate(num_list):
                diff = target - n
                if diff in numMap and numMap[diff] > i:
                    inner_res.append((prev,n,diff))
            return inner_res

        res = set()
        for i,n in enumerate(nums[0:len(nums)-1]):
            twoS = twoSum(nums[i+1:], 0-n, n)
            print(i,n,twoS)
            for l in twoS:
                res.add(l)

        
        return [list(s) for s in list(res)]

        



