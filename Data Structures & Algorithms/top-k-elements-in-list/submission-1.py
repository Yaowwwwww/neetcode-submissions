class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
                continue
            d[i] += 1

        return sorted(d, key = d.get, reverse=True)[0:k]
        