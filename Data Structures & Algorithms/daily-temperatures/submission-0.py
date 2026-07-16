class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((i,temp))
        
        return result