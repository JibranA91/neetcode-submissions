# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output_list = list()
        if len(pairs) > 0:
            output_list.append([p for p in pairs])
            for i in range(1,len(pairs)):            
                j = i
                while j > 0 and pairs[j-1].key > pairs[j].key:
                    pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
                    j -= 1
                output_list.append([p for p in pairs])
        return output_list