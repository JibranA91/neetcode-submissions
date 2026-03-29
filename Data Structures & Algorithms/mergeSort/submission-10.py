# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(arr, s, mid, e):
            i,j = s,mid
            merged_list = []
            while i < mid and j < e:
                if arr[i].key <= arr[j].key:
                    merged_list.append(arr[i])
                    i += 1
                else:
                    merged_list.append(arr[j])
                    j += 1
            merged_list += arr[i:mid] + arr[j:e]
            for k in range(len(merged_list)):
                arr[s+k] = merged_list[k]
            return arr

        def merge_sort(arr, s=0, e=None):
            if not e:
                e=len(arr)
            if e-s <= 1:
                return arr
            mid = (s+e)//2
            merge_sort(arr, s, mid)
            merge_sort(arr, mid, e)
            merge(arr, s, mid, e)
            return arr
        
        return merge_sort(pairs)