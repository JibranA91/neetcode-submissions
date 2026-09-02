class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1

        max_water = 0

        while L < R:
            min_h = min(heights[L], heights[R])
            water = (R-L)*min_h
            max_water = max(max_water, water)

            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1
        
        return max_water

