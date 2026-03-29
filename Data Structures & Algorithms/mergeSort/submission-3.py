# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(arr, s, mid, e):
            print([m.key for m in arr], s, mid,e)
            merge_list = []
            i,j = s,mid
            while i < mid and j < e:
                if arr[i].key <= arr[j].key:
                    merge_list.append(arr[i])
                    i += 1
                else:
                    merge_list.append(arr[j])
                    j += 1
            merge_list += arr[i:mid] + arr[j:e]

            for k in range(len(merge_list)):
                arr[s+k] = merge_list[k]

            print([m.key for m in arr])
            return 


        def merge_sort(arr, s=0, e=None):
            if e is None:
                e = len(arr)
            if e-s <= 1:
                return arr
        
            mid = (s+e)//2
            merge_sort(arr,s,mid)
            merge_sort(arr,mid,e)

            merge(arr, s, mid, e)

            return arr
        
        return merge_sort(pairs)
