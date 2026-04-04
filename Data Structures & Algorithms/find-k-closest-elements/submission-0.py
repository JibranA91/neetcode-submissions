class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        diff_arr = [(i, a - x) for i,a in enumerate(arr)]
        diff_arr = sorted(diff_arr, key=lambda x: (abs(x[1]),x[1]) )
        return sorted([arr[i[0]] for i in diff_arr[:k]])