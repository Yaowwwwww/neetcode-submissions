class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        return self.nums[self.k - 1]
