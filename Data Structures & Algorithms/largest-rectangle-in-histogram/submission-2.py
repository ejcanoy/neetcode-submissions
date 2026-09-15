class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i,n in enumerate(heights):
            index = i
            while stack and n <= stack[-1][1]:
                curI, curH = stack.pop()
                rect = (i - curI) * curH 
                maxArea = max(maxArea, rect)
                index = curI
            stack.append([index, n])
        
        for curI, curH in stack:
                    rect = (len(heights) - curI) * curH
                    maxArea = max(maxArea, rect)

        return maxArea


         