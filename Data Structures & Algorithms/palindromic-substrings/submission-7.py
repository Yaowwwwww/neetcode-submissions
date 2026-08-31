class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1
        for l in range(n - 1):
            r = l + 1
            if s[l] == s[r]:
                dp[l][r] = True
                count += 1
        print(count)
        for length in range(3, n + 1): #处理length3以上 aaaaa 3-5
            for l in range(n - length + 1):
                r = l + length - 1
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    count += 1
            print(count)
            
        return count