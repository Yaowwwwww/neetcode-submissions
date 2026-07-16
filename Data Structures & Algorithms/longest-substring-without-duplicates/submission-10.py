class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        cnt = 0
        Set = set()
        l = 0
        r = 0
        # print(len(s))
        while r < len(s):
            if s[r] in Set:
                l = l + 1
                r = l
                if cnt > Max:
                    Max = cnt
                Set = set()
                cnt = 0
                continue
            Set.add(s[r])
            
            cnt += 1

            r = r + 1
        if cnt > Max:
            Max = cnt

        return Max