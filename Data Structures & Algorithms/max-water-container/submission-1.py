class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        
        l = 0
        r = len(heights) - 1
        while(l < r):
            water = (r - l) * min(heights[l], heights[r])
            if water > result:
                result = water
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return result