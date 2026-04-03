class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_w = 0

        if heights:
            while L < R:
                w = min(heights[L], heights[R])*(R-L)
                max_w = max(max_w, w)

                if heights[L] < heights[R]:
                    L += 1
                else:
                    R -= 1

        return max_w