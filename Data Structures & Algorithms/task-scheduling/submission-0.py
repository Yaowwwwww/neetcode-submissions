class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for cnt in count.values():
            heapq.heappush(heap, -cnt)
        queue = deque()

        time = 1
        while heap or queue:
            #如果queue里的时间到点了 那就放回heap去继续处理
            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush(heap, freq)

            if heap:#heap有次数，那就减一然后放进queue去冷却
                freq = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    queue.append((freq, time + n + 1))
            time += 1
        return time - 1