class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse = True)
        stack = []
        print(cars)
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)

            