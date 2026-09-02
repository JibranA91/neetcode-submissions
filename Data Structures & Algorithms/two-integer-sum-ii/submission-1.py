class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ind_dict = {n:i for i,n in enumerate(numbers)}

        for i,n in enumerate(numbers):
            rem = target-n
            j = ind_dict.get(rem, -1)
            if i < j:
                return [i+1,j+1]