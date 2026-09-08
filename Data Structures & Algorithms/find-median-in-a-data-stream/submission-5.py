class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []


    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if len(self.left) > len(self.right) + 1: #处理left过多的失衡。
            popped = heapq.heappop(self.left)
            heapq.heappush(self.right, -popped)
        elif len(self.left) < len(self.right): #处理right过多的失衡。
            popped = heapq.heappop(self.right)
            heapq.heappush(self.left, -popped)


    def findMedian(self) -> float:
        if len(self.left) > len(self.right): 
            return -self.left[0] 
        else:
            return (-self.left[0] + self.right[0]) / 2
        