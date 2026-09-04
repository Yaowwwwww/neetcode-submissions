class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        dp_min = [0] * n
        dp_max = [0] * n
        dp_min[0] = dp_max[0] = nums[0] if nums else 0
        for i in range(1, n):
            cur = nums[i]
            dp_max[i] = max(cur, cur * dp_max[i - 1], cur * dp_min[i - 1])
            dp_min[i] = min(cur, cur * dp_min[i - 1], cur * dp_max[i - 1])

        return max(dp_max)
