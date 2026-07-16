class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backTracking(openCnt, closeCnt):
            if openCnt == closeCnt == n:
                result.append("".join(stack))
                return 

            if openCnt < n:
                stack.append("(")
                backTracking(openCnt + 1, closeCnt)
                stack.pop()
            if closeCnt < openCnt:
                stack.append(")")
                backTracking(openCnt, closeCnt + 1)
                stack.pop()

        backTracking(0,0)
        return result