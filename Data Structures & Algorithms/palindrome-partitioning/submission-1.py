class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        valid_trail = []

        def isPal(w):
            if w == None:
                return False
            return w == w[::-1]

        def dfs(startIndex):
            print(startIndex)
            if startIndex == len(s):
                print(valid_trail)
                res.append(valid_trail[:])
                print(res)
                return

            #单层循环逻辑
            for i in range(startIndex + 1, len(s) + 1):
                w = s[startIndex:i]
                print(w)
                print(isPal(w))
                if isPal(w):
                    valid_trail.append(w)
                else:
                    continue#剪枝

                #回溯逻辑
                dfs(i)
                valid_trail.pop()

        dfs(0)
        return res