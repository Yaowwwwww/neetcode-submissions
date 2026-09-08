class MedianFinder:

    def __init__(self):
        self.arr = []


    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        length = len(self.arr)
        self.arr.sort()
        return self.arr[length // 2] if length % 2 != 0 else (self.arr[(length // 2) - 1] + self.arr[(length // 2)]) / 2
        