class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heap.append([x ** 2 + y ** 2, x, y])
        
        heapq.heapify(heap)

        result = []

        for i in range(k):
            point = heapq.heappop(heap)
            result.append([point[1], point[2]])

        return result