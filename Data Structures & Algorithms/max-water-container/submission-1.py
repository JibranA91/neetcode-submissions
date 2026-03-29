class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j= 0, len(heights)-1
        max_area = 0
        while i < j:
            h_i, h_j = heights[i], heights[j]
            area = min(h_i, h_j) * (j - i)
            print(h_i, h_j, area)
            max_area = max(max_area, area)
            if h_i < h_j:
                i += 1
            else:
                j -= 1
        
        return max_area