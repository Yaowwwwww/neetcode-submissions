class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums[:]
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k: 
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) == self.k:
            heapq.heappush(self.min_heap, val)
            heapq.heappop(self.min_heap)
        return self.min_heap[0]