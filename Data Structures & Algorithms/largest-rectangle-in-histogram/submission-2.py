class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def calculateArea(width, height):
            return width * height

        maxArea = 0
        stack = []

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                prevIndex, prevHeight = stack.pop()
                area = calculateArea(index - prevIndex, prevHeight)
                maxArea = max(maxArea, area)
                start = prevIndex
            stack.append((start, height))

        while stack:
            area = calculateArea(len(heights) - stack[-1][0], stack[-1][1])
            maxArea = max(maxArea, area)
            stack.pop()
        
        return maxArea