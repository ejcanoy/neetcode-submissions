class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxTotal = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxTotal = max(area, maxTotal)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxTotal