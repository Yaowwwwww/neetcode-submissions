class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxWindow = 0
        l, r = 0, 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            
            windowSize = r - l + 1
            if windowSize - count.get(max(count, key = count.get)) <= k:
                maxWindow = max(maxWindow, windowSize)
            else:
                count[s[l]] = count[s[l]] - 1
                l = l + 1
            r = r + 1
        
        return maxWindow