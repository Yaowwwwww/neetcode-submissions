class Solution:
    def longestPalindrome(self, s: str) -> str:
        #初始化全False DP 2d array
        dp = [[False] * len(s) for _ in range(len(s))]

        #初始化对角为True
        for x in range(len(s)):
            dp[x][x] = True
        
        #生成完整dp, 从length1开始考虑，每次从i开始到j结束,比如aba
        # 0,0 1,1, 2,2
        # 0,1 1,2
        # 0,2
        # 顺便每次比较长度记住去判断最长即可

        start = 0
        maxLen = 1
        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                currLen = j - i + 1
                if dp[i][j] and currLen > maxLen:
                    start = i
                    maxLen = length
        
        return s[start: start + maxLen]



