class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1
        
        maxL = height[l]
        maxR = height[r]
        # min(maxleft, maxright) - currheight
        while(l <= r):
            if maxL < maxR: 

                adding = maxL - height[l]
                if adding > 0:
                    result += adding

                if maxL < height[l]:
                    maxL = height[l]
                l += 1

            elif maxL >= maxR:

                adding = maxR - height[r]
                if adding > 0:
                    result += adding

                if maxR < height[r]:
                    maxR = height[r] 
                r -= 1

        return result